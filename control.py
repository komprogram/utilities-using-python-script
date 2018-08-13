#Use IDLE python command prompt for running the script.
#This python script is solely created for Windows OS. 

import os

#Shuts the system down
def shutdown():
	os.system("shutdown -s")

#Restarts the system 
def restart():
	os.system("shutdown -r")	

#Logoff from the system
def logoff():
	os.system("shutdown -l")

#Open the command prompt to compile and run programs, access files, create folders, etc.
def cmd():
	os.system("cmd.exe")

def main():
		operation = input("What do u want to do (1.shutdown, 2.restart, 3.logoff, 4.open cmd ) :")
		if(operation!='1' and operation!='2' and operation!='3' and operation!='4'):
			print("You must enter a valid operation!")
		else:
			if(operation == '1'):
				shutdown()
			elif(operation == '2'):
				restart()
			elif(operation == '3'):
				logoff()
			else:
				cmd()
			
main()
input()