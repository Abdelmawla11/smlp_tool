#/user bin
import os
from time import *
import sys 

######################################

################$#color###############


b="\033[0;34m"
g="\033[1;32m"
w="\033[1;37m"
r="\033[1;31m"
y="\033[1;33m"
cyan = "\033[0;36m"
lgray = "\033[0;37m"
dgray = "\033[1;30m"
ir = "\033[0;101m"
reset = "\033[0m"



os.system("clear")
print("""             =======( )=======()=======
     	 ===========()=========()===========
    ========= Abdel     Mawla   ===============
        ===========( )=======()============
             =======()=========()======
     	""")


sleep(3);os.system("clear")


print( r+'》》》》》Enter you choise 《《《《《'.center(60))
				
def choice():
	print('[1]	Update & Upgrade'.center(60))
	print('[2]	Install Packages'.center(60))
	print('[3]	Install tools   '.center(60))
	print('[0]	Exit		'.center(50))
choice()


choice=int(input( y+"Enter your choice ==> "))

while choice != 0:
	if choice == 1:
		print(w+"\n[*]" + "witeing Update")
		print(g+'\n[*]' + 'Updating...')
		os.system("apt update")
		print('[*]' + 'Packages updated')
		print('\n[*]' + 'Upgrading...')
		os.system("apt install git -y")
		print('\n[*]' + w + 'Packages upgraded...')
		print('[*]' + r + ' Packages updated & upgraded ... ! ')
	elif choice == 2:
		print(r+ '\n[+] ' +g+ 'Installing git ... !')
		os.system('apt install git -y')
		print(r+ '[*] ' +g+ 'git package installed .')
		print(r+ '\n[+] ' +g+ 'Installing nano package...')
		os.system('apt install nano -y')
		print(r+ '[*] ' +g+ 'wget package installed.')
		print(r+ '\n[+] ' +g+ 'nano stalling curl package...')
		os.system('apt install python-y')
		print(r+ '[*] ' +g+ 'python package installed.')
		print(r+ '\n[+] ' +g+ 'Installing python2 package...')
		os.system('apt install python2 -y')
		print(r+ '[*] ' +g+ 'python2 package installed.')
		print(r+ '\n[+] ' +g+ 'Installing zip package...')
		os.system('apt install zip -y')
		print(r+ '[*] ' +g+ 'zip package installed.')
		print(r+ '\n[+] ' +g+ 'Installing unzip package...')
		os.system('apt install unzip -y')
		print(r+ '[*] ' +g+ 'unzip  package installed.')
		print(r+ '\n[+] ' +g+ 'Installing pip package...')
		os.system('apt install pip -y')
		print(r+ '[*] ' +g+ 'pip  package installed.')
		print(r+ '\n[+] ' +g+ 'Installing tor package...')
		os.system('apt install tor -y')
		print(r+ '[*] ' +g+ 'tor package installed.')
		print(r+ '\n[+] ' +g+ 'Installing tor package...')
		os.system('apt install wget -y')
		print(r+ '[*] ' +g+ 'wget package installed.')
		print(r+ '\n[+] ' +g+ 'Installing nmap package...')
		os.system('apt install nmap -y')
		print(r+ '[*] ' +g+ 'nmap package installed.')
	elif choice == 3:
		def Tool():
			print('[1]      Tool-X'.center(60))
			print('[2]      Lazymux'.center(60))
			print('[0]      Exit            '.center(50))
		Tool()

		Tool=int(input('Enter your Tool Number >> '))
		if Tool == 1:
			print('Insralling Tool-X >>')
			os.system('git clone https://github.com/rajkumardusad/Tool-X')
		elif Tool ==2:
			print('Installing lazymox >>')
			os.system('git clone https://github.com/Gameye98/Lazymux')
		elif Tool ==0:
			os.system('exit')
		else:
			print('command not found')
	elif choice ==0:
                os.system('exit')
	else:
                print('command not found')



