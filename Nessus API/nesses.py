import requests
import json
import time
import sys
import os
import re

#对数据库里所有IP扫描得到不重复的pluginID再根据pluginID得到漏洞详细信息文件


es = ['192.168.1.1']
url = 'https://localhost:8834'
verify = False
token = ''
username = 'zhang'#你的账号
password = '**********'#你的密码
para = {
    "_source":"ip"
}

def build_url(resource):
    return '{0}{1}'.format(url, resource)

def connect(method, resource, data=None):
    """
    Send a request
    Send a request to Nessus based on the specified data. If the session token
    is available add it to the request. Specify the content type as JSON and
    convert the data to JSON format.
    """
    headers = {'X-Cookie': 'token={0}'.format(token),
               'content-type': 'application/json'}

    data = json.dumps(data)

    if method == 'POST':
        r = requests.post(build_url(resource), data=data, headers=headers, verify=verify)
    elif method == 'PUT':
        r = requests.put(build_url(resource), data=data, headers=headers, verify=verify)
    elif method == 'DELETE':
        r = requests.delete(build_url(resource), data=data, headers=headers, verify=verify)
    else:
        r = requests.get(build_url(resource), params=data, headers=headers, verify=verify)

    # Exit if there is an error.
    if r.status_code != 200:
        e = r.json()
        print (e['error'])
        sys.exit()

    # When downloading a scan we need the raw contents not the JSON data.
    if 'download' in resource:
        return r.content
    else:
        return r.json()

def login(usr, pwd):
    """
    Login to nessus.
    """

    login = {'username': usr, 'password': pwd}
    data = connect('POST', '/session', data=login)

    return data['token']

def logout():
    """
    Logout of nessus.
    """

    connect('DELETE', '/session')

def get_policies():
    """
    Get scan policies
    Get all of the scan policies but return only the title and the uuid of
    each policy.
    """

    data = connect('GET', '/editor/policy/templates')

    return dict((p['title'], p['uuid']) for p in data['templates'])

def get_history_ids(sid):
    """
    Get history ids
    Create a dictionary of scan uuids and history ids so we can lookup the
    history id by uuid.
    """
    data = connect('GET', '/scans/{0}'.format(sid))

    return dict((h['uuid'], h['history_id']) for h in data['history'])

def get_scan_history(sid, hid):
    """
    Scan history details
    Get the details of a particular run of a scan.
    """
    params = {'history_id': hid}
    data = connect('GET', '/scans/{0}'.format(sid), params)

    return data['info']

def add(name, desc, targets, pid):
    """
    Add a new scan
    Create a new scan using the policy_id, name, description and targets. The
    scan will be created in the default folder for the user. Return the id of
    the newly created scan.
    """

    scan = {'uuid': pid,
            'settings': {
                'name': name,
                'description': desc,
                'text_targets': targets}
            }

    data = connect('POST', '/scans', data=scan)

    return data['scan']

def update(scan_id, name, desc, targets, pid=None):
    """
    Update a scan
    Update the name, description, targets, or policy of the specified scan. If
    the name and description are not set, then the policy name and description
    will be set to None after the update. In addition the targets value must
    be set or you will get an "Invalid 'targets' field" error.
    """
    scan = {}
    scan['settings'] = {}
    scan['settings']['name'] = name
    scan['settings']['desc'] = desc
    scan['settings']['text_targets'] = targets

    if pid is not None:
        scan['uuid'] = pid

    data = connect('PUT', '/scans/{0}'.format(scan_id), data=scan)

    return data

def launch(sid):
    """
    Launch a scan
    Launch the scan specified by the sid.
    """

    data = connect('POST', '/scans/{0}/launch'.format(sid))

    return data['scan_uuid']

def status(sid, hid):
    """
    Check the status of a scan run
    Get the historical information for the particular scan and hid. Return
    the status if available. If not return unknown.
    """

    d = get_scan_history(sid, hid)
    return d['status']

def export_status(sid, fid):
    """
    Check export status
    Check to see if the export is ready for download.
    """

    data = connect('GET', '/scans/{0}/export/{1}/status'.format(sid, fid))

    return data['status'] == 'ready'

def export(sid, hid):
    """
    Make an export request
    Request an export of the scan results for the specified scan and
    historical run. In this case the format is hard coded as nessus but the
    format can be any one of nessus, html, pdf, csv, or db. Once the request
    is made, we have to wait for the export to be ready.
    """
    data = {'history_id': hid,
            'format': 'nessus'}

    data = connect('POST', '/scans/{0}/export'.format(sid), data=data)

    fid = data['file']

    while export_status(sid, fid) is False:
        time.sleep(5)

    return fid

def download(sid, fid):
    """
    Download the scan results
    Download the scan results stored in the export file specified by fid for
    the scan specified by sid.
    """
    data = connect('GET', '/scans/{0}/export/{1}/download'.format(sid, fid))
    filename = 'nessus_{0}_{1}.nessus'.format(sid, fid)

    print('Saving scan results to {0}.'.format(filename))
    with open(filename, 'w') as f:
        f.write(data)
    return filename

def extract(file):
    outfile = 'output.txt'
    count = 0
    lines_seen = set()
    in_file = open(file, 'r')
    out_file = open(outfile, 'a')
    lines = in_file.readlines()

    for line in lines:
        if line not in lines_seen:
            str_name = line.split(" ")[0]
            str1 = 'pluginId'
            if (str1 in str_name):
                out_file.write(line)
                count += 1
            lines_seen.add(line)
    in_file.close()
    out_file.close()
    os.remove(file)
    return outfile

def get_vul_detail(file):
    vul_detail = {
        "cve_number": "",
        "vul_name": "",
        "vul_intro": "",
        "vul_detail": "",
        "vul_level": 0,
        "solution":"",
        "release_time": "",
        "discover_time": ""
    }
    header = {'X-Cookie': 'token={0}'.format(token),
               'content-type': 'application/json'}
    endfile = 'endfile.txt'
    id_file = open(file, 'r')
    detail_file = open(endfile,'w')
    end = open('end.txt','w+')
    str1 = r'\''
    str2 = r'"'

    lines = id_file.readlines()
    for line in lines:
        m = re.findall(r'(\w*[0-9]+)\w*', line)
        plugin_id = m[0]
        url = 'https://localhost:8834/plugins/plugin/{plugin_id}'.format(plugin_id=plugin_id)
        respone = requests.get(url, headers=header, verify=False)
        if respone is not None:
            result = json.loads(respone.text)
            # 漏洞名称
            vul_detail['vul_name'] = str(result['name']).encode('utf-8')
            # 遍历attributes生成结果
            for attr in result['attributes']:
                attr_name = attr['attribute_name']
                # cve编号
                if attr_name == 'cve':
                    vul_detail['cve_number'] = str(attr['attribute_value']).encode('utf-8')
                    continue
                # 漏洞描述
                elif attr_name == 'synopsis':
                    vul_detail['vul_intro'] = str(attr['attribute_value']).encode('utf-8')
                    continue
                # 漏洞详情
                elif attr_name == 'description':
                    vul_detail['vul_detail'] = str(attr['attribute_value']).encode('utf-8')
                    continue
                # 漏洞等级
                elif attr_name == 'risk_factor':
                    vul_detail['risk_factor'] = str(attr['attribute_value']).encode('utf-8')
                    continue
                # 漏洞描述
                elif attr_name == 'solution':
                    vul_detail['solution'] = str(attr['attribute_value']).encode('utf-8')
                    continue
                # 漏洞发布时间
                elif attr_name == 'plugin_publication_date':
                    vul_detail['release_time'] = str(attr['attribute_value']).encode('utf-8')
                    continue
                # 漏洞发现时间
                elif attr_name == 'vuln_publication_date':
                    vul_detail['discover_time'] = str(attr['attribute_value']).encode('utf-8')
                    continue
            detail_file.write(str(vul_detail)+'\n')
    detail_file.close()
    detail_file = open(endfile, 'r')
    for ss in detail_file.readlines():
        tt = re.sub(str1, str2, ss)
        end.write(tt)
    id_file.close()
    detail_file.close()
    end.close()
    os.remove(endfile)
    #os.remove(file)

if __name__ == '__main__':
    file_puginid = ''
    print('Login')
    token = login(username, password)
    m = 0
    flag = 0


    s = es


    for ip in s:
        IPdone = open('IP.txt', 'a+')
        lines = IPdone.readlines()
        ss = str(ip).encode('utf-8')

        IPdone.close()

        if m == 0:
            flag = 1
            IPdone = open('IP.txt', 'a')
            IPdone.write(ss)
            IPdone.close()
            # print('Adding new scan.')
            policies = get_policies()
            policy_id = policies['Basic Network Scan']
            scan_data = add('Test Scan', 'Create a new scan with API', '192.168.1.1', policy_id)
            scan_id = scan_data['id']

            # print('Updating scan with new targets.')
            update(scan_id, scan_data['name'], scan_data['description'], ip)
            print(ip)
            # print('Launching new scan.')
            scan_uuid = launch(scan_id)
            history_ids = get_history_ids(scan_id)
            history_id = history_ids[scan_uuid]
            while status(scan_id, history_id) != 'completed':
                time.sleep(5)

            # print('Exporting the completed scan.')
            file_id = export(scan_id, history_id)
            filename = download(scan_id, file_id)
            file_puginid = extract(filename)
    if flag == 1:
        get_vul_detail(file_puginid)