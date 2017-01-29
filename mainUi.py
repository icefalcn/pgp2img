#!/usr/bin/env python

import os
import sys
import subprocess
import re

ASKII_ART = "$$$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$\  $$$$$$\ $$\      $$\  $$$$$$\ \n$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ \_$$  _|$$$\    $$$ |$$  __$$\ \n$$ |  $$ |$$ /  \__|$$ |  $$ |\__/  $$ |  $$ |  $$$$\  $$$$ |$$ /  \__|\n$$$$$$$  |$$ |$$$$\ $$$$$$$  | $$$$$$  |  $$ |  $$\$$\$$ $$ |$$ |$$$$\ \n$$  ____/ $$ |\_$$ |$$  ____/ $$  ____/   $$ |  $$ \$$$  $$ |$$ |\_$$ |\n$$ |      $$ |  $$ |$$ |      $$ |        $$ |  $$ |\$  /$$ |$$ |  $$ |\n$$ |      \$$$$$$  |$$ |      $$$$$$$$\ $$$$$$\ $$ | \_/ $$ |\$$$$$$  |\n\__|       \______/ \__|      \________|\______|\__|     \__| \______/"
DIVIDER = "---------------------------------------------------------------------------"

def printBanner():
	print DIVIDER
	print ASKII_ART
	print "\nPGP2IMG V0.1\tM. Liu, T. Voinea, J. Leger\tMcHacks 2017"
	print "\"\"In Encryption we trust\" -Wayne Gretzky\" - Michael Scott"
	print DIVIDER

def printHelp():
	print """\nNAME:\n\tPGP2IMG - A picture is worth a thousand encrypted words\n\nVERSION:\n\t0.1\n\nCOMMANDS:\n\tencrypt\t\tEncrypt messages in messages for keybase users\n\t\t\t[Keybase user] [Message] [File path]\n\n\tdecrypt\t\tDecrypt hidden message inside images\n\t\t\t[File path]\n"""

def encryptMessage(recipient, message, transportFile):
	printBanner()
	message = os.system("keybase pgp encrypt " + recipient + " -m \"" + message +"\" | tr '[A-Z]' '[X-ZA-W]' >> " + str(transportFile))
	print "message successfully encrypted"

def encryptFile(recipient, payloadFile, transportFile):
	printBanner()
	print "recepient = "+ recipient + " payloadFile = " + payloadFile + "transportFile = " + transportFile
	message = os.system("keybase encrypt " + recipient + " -i \"" + payloadFile +"\" >> " + str(transportFile))
	os.system("echo \"" + payloadFile.upper().split('/')[-1] +"\" >> " + transportFile)
	print "file successfully encrypted"

def getEncryptedMessage(content):
	regex= re.compile('-----YBDFK MDM JBPPXDB-----[.\S\s]{1,}-----BKA MDM JBPPXDB-----')
	match = regex.findall(content)
	return match

def decryptMessage(transportFile):
	content = subprocess.check_output(['cat', transportFile])
	match = getEncryptedMessage(content)
	if len(match) != 0:
		os.system("echo \""+ match[0] + "\" | tr '[X-ZA-W]' '[A-Z]' > tempyMcTempFace.txt")
		pgp = subprocess.check_output(['cat', 'tempyMcTempFace.txt'])
		print "Encrypted message: " + subprocess.check_output(['keybase', 'pgp', 'decrypt', '-m',pgp])
	else:
		print "no hidden message found"

def decryptFile(transportFile):
	content = subprocess.check_output(['cat', transportFile])
	regex= re.compile('BEGIN KEYBASE SALTPACK ENCRYPTED MESSAGE[.][.\S\s]{1,}END KEYBASE SALTPACK ENCRYPTED MESSAGE[.]')
	match = regex.findall(content)
	if(len(match)!=0):
		regexName= re.compile('BEGIN KEYBASE SALTPACK ENCRYPTED MESSAGE[.][.\S\s]{1,}END KEYBASE SALTPACK ENCRYPTED MESSAGE[.]\n(.*)')
		matchName = regexName.findall(content)
		print matchName
		match[0] +="\n"	
		tempFile = open("temp.txt","w")
		tempFile.write(match[0])
		tempFile.close()
		print "cat temp.txt | keybase decrypt -o "+ matchName[0]
		os.system("cat temp.txt | keybase decrypt -o "+ matchName[0])
		os.remove("temp.txt")
	else: 
		print "no hidden file found"
'''
#user selects option to encrypt a file.
if len(sys.argv) == 6 and sys.argv[1] == "encrypt" and sys.argv[2] == "-i":
	if os.path.isfile(sys.argv[4]) and os.path.isfile(sys.argv[5]):
		encryptFile()
	else:
		print "the file path does not exist"

#user selects option to encrypt a message.
elif len(sys.argv) == 6 and sys.argv[1] == "encrypt" and sys.argv[2] == "-m":
	if os.path.isfile(sys.argv[5]):
		encryptMessage()
	else:
		print "the file path does not exist"

#user selects option to decrypt file
elif len(sys.argv) == 3 and sys.argv[1] == "decrypt":
	printBanner()
	if os.path.isfile(sys.argv[2]):

		if (len(match)!=0):
			decryptMessage(match);
		else:
			content = subprocess.check_output(['cat', sys.argv[2]])
			match = getEcryptedFile(content)
			if(len(match)!=0):
				decryptFile(match)
			else:
				print "no hidden message found"
	else:
		print "invalid file"
elif len(sys.argv) == 1 or sys.argv[1] == "help":
	printHelp()
else:
	print "INVALID ARGUMENTS"
	printHelp()'''