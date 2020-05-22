#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ LIBRERIAS $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
import time
import sys
import os
from io import open

# Programador David soto noche
# Correo: Sotodelanoche@gmail.com
# Lenguaje Python3 scrispt 
# Fecha 19:04:2020:
# Nombre del programa : ExploX_TelneT_BrtFor
# Accion: explotacion de servidores atraves de telnet MSF5

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ SETUP $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def install():

	os.system('sudo apt-get install xinetd telnetd')
	os.system('echo "telnet stream tcp nowait telnetd /usr/sbin/tcpd /usr/sbin/in.telnetd" > /etc/inetd.conf')
	os.system('rm /etc/xinetd.conf')
	file = open("/etc/xinetd.conf","w")
	file.write('# Simple configuration file for xinetd'+'\n')
	file.write('#'+'\n')
	file.write('# Some defaults, and include /etc/xinetd.d/'+'\n')
	file.write('defaults'+'\n')
	file.write('{'+'\n')
	file.write('# Please note that you need a log_type line to be able to use log_on_success'+'\n')
	file.write('# and log_on_failure. The default is the following :'+'\n')
	file.write('# log_type = SYSLOG daemon info'+'\n')
	file.write('instances = 60'+'\n')
	file.write('log_type = SYSLOG authpriv'+'\n')
	file.write('log_on_success = HOST PID'+'\n')
	file.write('log_on_failure = HOST'+'\n')
	file.write('cps = 25 30'+'\n')
	file.write('}'+'\n')
	file.write('includedir /etc/xinetd.d'+'\n')
	time.sleep(1)
	os.system('sudo /etc/init.d/xinetd restart')

install()
