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

def encryptMessage():
	printBanner()
	message = os.system("keybase pgp encrypt " + sys.argv[3] + " -m \"" + sys.argv[4] +"\" | tr '[A-Z]' '[X-ZA-W]' >> " + str(sys.argv[5]))
	print "message successfully encrypted"

def encryptFile():
	printBanner()
	message = os.system("keybase encrypt " + sys.argv[3] + " -i \"" + sys.argv[4] +"\" >> " + str(sys.argv[5]))
	os.system("echo \"" + sys.argv[4].upper() +"\" >> " + sys.argv[5])
	if len(sys.argv) == 7:
		os.system("cp " + sys.argv[5] + " /keybase/private/" + sys.argv[6] + "," + sys.argv[3])
	print "file successfully encrypted"

def getEncryptedFile(content):
	regex= re.compile('BEGIN KEYBASE SALTPACK ENCRYPTED MESSAGE[.][.\S\s]{1,}END KEYBASE SALTPACK ENCRYPTED MESSAGE[.]')
	match = regex.findall(content)
	return match

def decryptFile(match):
	regexName= re.compile('BEGIN KEYBASE SALTPACK ENCRYPTED MESSAGE[.][.\S\s]{1,}END KEYBASE SALTPACK ENCRYPTED MESSAGE[.]\n(.*)')
	matchName = regexName.findall(content)
	print matchName
	match[0] +="\n"
	#print match[0]
	tempFile = open("temp.txt","w")
	tempFile.write(match[0])
	tempFile.close()
	print "cat temp.txt | keybase decrypt -o "+ matchName[0]
	os.system("cat temp.txt | keybase decrypt -o "+ matchName[0])
	os.remove("temp.txt")

def getEncryptedMessage(content):
	regex= re.compile('-----YBDFK MDM JBPPXDB-----[.\S\s]{1,}-----BKA MDM JBPPXDB-----')
	match = regex.findall(content)
	return match

def decryptMessage(match):
	os.system("echo \""+ match[0] + "\" | tr '[X-ZA-W]' '[A-Z]' > tempyMcTempFace.txt")
	pgp = subprocess.check_output(['cat', 'tempyMcTempFace.txt'])
	pgp = pgp
	print "Encrypted message: " + subprocess.check_output(['keybase', 'pgp', 'decrypt', '-m',pgp])

#user selects option to encrypt a file.
if (len(sys.argv) == 6 or len(sys.argv) == 7) and sys.argv[1] == "encrypt" and sys.argv[2] == "-i":
	if os.path.isfile(sys.argv[4]) and os.path.isfile(sys.argv[5]):
		encryptFile()
	else:
		print "the file path does not exist"

#user selects option to encrypt a message.
elif (len(sys.argv) == 6 or len(sys.argv) == 7) and sys.argv[1] == "encrypt" and sys.argv[2] == "-m":
	if os.path.isfile(sys.argv[5]):
		encryptMessage()
	else:
		print "the file path does not exist"

#user selects option to decrypt file
elif len(sys.argv) == 3 and sys.argv[1] == "decrypt":
	printBanner()
	if os.path.isfile(sys.argv[2]):
		content = subprocess.check_output(['cat', sys.argv[2]])
		match = getEncryptedFile(content)
		if (len(match)!=0):
			decryptFile(match);
		else:
			content = subprocess.check_output(['cat', sys.argv[2]])
			match = getEncryptedMessage(content)
			if(len(match)!=0):
				decryptMessage	(match)
			else:
				print "no hidden message found"
	else:
		print "invalid file"
elif len(sys.argv) == 1 or sys.argv[1] == "help":
	printHelp()
else:
	print "INVALID ARGUMENTS"
	printHelp()
