import sys
import os
def sds(config):
    config=open('ness.rc','w')#首先我们来创建一个xxx.rc的文件
   #把你要使用到的模块和对应的参数写入xxx.rc里去
    config.write('load nessus'+"\n")
    config.write('nessus_connect Nessus:Nessus@127.0.0.1:8834 ok'+"\n")#账号：密码
    config.write('nessus_save'+"\n")
    config.write('nessus_scan_new 731a8e52-3ea6-a291-ec0a-d2ff0619c19d7bd788d6be818b65 test test 10.10.10.134 '+"\n")#ip需要修改以及策略提前建立
    config.write('nessus_scan_launch 12'+"\n")#参数要提前确立修改
    config.write('nessus_report_hosts 12'+"\n")

    config.write('nessus_scan_enport 12 Nessus'+"\n")
    config.write('nessus_report_dowload 12 482612627'+"\n")
    config.write('nessus_db_import 12'+"\n")
    config.write('db_import /root/.msf4/local/12-482612627'+"\n")
    #config.write('load_db_autopwn'+"\n")
    #config.write('db_autopwn -t -p -e -r'+"\n")
    #config.write('sessions 1'+"\n")
sds('')
def main():
    mg=os.system('msfconsole -r /root/ness.rc')#执行msfconsole -r 路径/xxx.rc,就可以了

if __name__ == '__main__':
    main()