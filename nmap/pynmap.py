#!/usr/bin/env python

import nmap
import pymongo
import csv
import time
scan_range = '192.168.186.128'  #扫描目标
scan_ports = '22,23,53,80,443,445'  #端口多个端口逗号隔开，范围用‘-’分隔

nm = nmap.PortScanner()
nm.scan(scan_range, scan_ports)


# print result as CSV
f = nm.csv()
print(f)

#写入csv文件
#引入时间命名文件
fr = f.replace(";",",")    #转为csv的格式    用‘，’替换‘;’

now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
fname = now+r"report.csv"

st = open(fname, "w")
st.write(fr)
st.close()

#csv文件转字典格式数据存入数据库
with open(fname,'r',encoding='utf-8')as csvfile:
    reader=csv.DictReader(csvfile)
    counts=0
    for each in reader:
        each['host']=each['host']
        each['hostname']=each['hostname']
        each['hostname_type']=each['hostname_type']
        each['protocol']=each['protocol']
        each['port']=each['port']
        each['name']=each['name']
        each['state']=each['state']
        each['product'] = each['product']
        each['extrainfo'] = each['extrainfo']
        each['reason'] = each['reason']
        each['version'] = each['conf']
        each['conf'] = each['conf']
        each['cpe'] = each['cpe']
# 连接数据库写入数据
        client = pymongo.MongoClient(host='localhost', port=27017)
        db = client.nmapy
        set = db.scanre
        set.insert_one(each)

        counts+=1
    print('成功添加了'+str(counts)+'条数据')


