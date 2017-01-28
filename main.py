#!/usr/bin/env python

import os
import sys
import subprocess
import re
if len(sys.argv) == 5 and sys.argv[1] == "encrypt" :
	if os.path.isfile(sys.argv[4]):
		print "---------------------------------------------------------------------------"
		print "$$$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$\  $$$$$$\ $$\      $$\  $$$$$$\ \n$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ \_$$  _|$$$\    $$$ |$$  __$$\ \n$$ |  $$ |$$ /  \__|$$ |  $$ |\__/  $$ |  $$ |  $$$$\  $$$$ |$$ /  \__|\n$$$$$$$  |$$ |$$$$\ $$$$$$$  | $$$$$$  |  $$ |  $$\$$\$$ $$ |$$ |$$$$\ \n$$  ____/ $$ |\_$$ |$$  ____/ $$  ____/   $$ |  $$ \$$$  $$ |$$ |\_$$ |\n$$ |      $$ |  $$ |$$ |      $$ |        $$ |  $$ |\$  /$$ |$$ |  $$ |\n$$ |      \$$$$$$  |$$ |      $$$$$$$$\ $$$$$$\ $$ | \_/ $$ |\$$$$$$  |\n\__|       \______/ \__|      \________|\______|\__|     \__| \______/"
		print "\nPGP2IMG V0.1\tM. Liu, T. Voinea, J. Leger\tMcHacks 2017"
		print "\"I have a son. He's 10 years old. He has computers\" - President Trump"
		print "---------------------------------------------------------------------------"
		#check if the path exist and id we can write to it
		message = os.system("keybase encrypt " + sys.argv[2] + " -i \"" + sys.argv[3] +"\" >> " + str(sys.argv[4]))
		os.system("echo \"" + sys.argv[3].upper() +"\" >> " + sys.argv[4])
		print "message successfully encrypted"
	else:
		print "the file path does not exist"
elif len(sys.argv) == 3 and sys.argv[1] == "decrypt":
	print "---------------------------------------------------------------------------"
	print "$$$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$\  $$$$$$\ $$\      $$\  $$$$$$\ \n$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ \_$$  _|$$$\    $$$ |$$  __$$\ \n$$ |  $$ |$$ /  \__|$$ |  $$ |\__/  $$ |  $$ |  $$$$\  $$$$ |$$ /  \__|\n$$$$$$$  |$$ |$$$$\ $$$$$$$  | $$$$$$  |  $$ |  $$\$$\$$ $$ |$$ |$$$$\ \n$$  ____/ $$ |\_$$ |$$  ____/ $$  ____/   $$ |  $$ \$$$  $$ |$$ |\_$$ |\n$$ |      $$ |  $$ |$$ |      $$ |        $$ |  $$ |\$  /$$ |$$ |  $$ |\n$$ |      \$$$$$$  |$$ |      $$$$$$$$\ $$$$$$\ $$ | \_/ $$ |\$$$$$$  |\n\__|       \______/ \__|      \________|\______|\__|     \__| \______/"
	print "\nPGP2IMG V0.1\tM. Liu, T. Voinea, J. Leger\tMcHacks 2017"
	print "\"I have a son. He's 10 years old. He has computers\" - President Trump"
	print "---------------------------------------------------------------------------"
	if os.path.isfile(sys.argv[2]):
		content = subprocess.check_output(['cat', sys.argv[2]])
		regex= re.compile('BEGIN KEYBASE SALTPACK ENCRYPTED MESSAGE[.][.\S\s]{1,}END KEYBASE SALTPACK ENCRYPTED MESSAGE[.]')
		match = regex.findall(content)
		regexName= re.compile('BEGIN KEYBASE SALTPACK ENCRYPTED MESSAGE[.][.\S\s]{1,}END KEYBASE SALTPACK ENCRYPTED MESSAGE[.]\n(.*)')
		matchName = regexName.findall(content)
		if len(match) == 0:
			print "no hidden message found"
		else:
			match[0] +="\n"
			print match[0]
			tempFile = open("temp.txt","w")
			tempFile.write(match[0])
			tempFile.close()
			print "cat temp.txt | keybase decrypt -o "+ matchName[0]
			os.system("cat temp.txt | keybase decrypt -o "+ matchName[0])
			os.remove("temp.txt")
	else:
		print "invalid file"
elif len(sys.argv) == 1 or sys.argv[1] == "help":
	print "\nNAME:\n\tPGP2IMG - A picture is worth a thousand encrypted words\n\nVERSION:\n\t0.1\n\nCOMMANDS:\n\tencrypt\t\tEncrypt messages in messages for keybase users\n\t\t\t[Keybase user] [Message] [File path]\n\n\tdecrypt\t\tDecrypt hidden message inside images\n\t\t\t[File path]\n"
else:
	print "INVALID ARGUMENTS"
	print "\nNAME:\n\tPGP2IMG - A picture is worth a thousand encrypted words\n\nVERSION:\n\t0.1\n\nCOMMANDS:\n\tencrypt\t\tEncrypt messages in messages for keybase users\n\t\t\t[Keybase user] [Message] [File path]\n\n\tdecrypt\t\tDecrypt hidden message inside images\n\t\t\t[File path]\n"
