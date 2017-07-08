import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from os import stat
import os.path

def sendEmail(myEmail,myPass,subject):
	contacts = []
	message = MIMEMultipart()

	if(stat("contacts.txt").st_size == 0):
		print("contacts.txt is empty")
	else:
		# store contacts list
		with open("contacts.txt") as getContacts:
			contacts = [line.strip() for line in getContacts]

	if(stat("msg.txt").st_size == 0):
		print("msg.txt is empty")
	else:
		with open("msg.txt","r") as messageFile:
			myMessage = messageFile.read()

	print("Do you want to include an image : ? y/n")
	answ = input()
	if(answ == "y"):
		print("Enter image's name :")
		imageName = input()
		if(os.path.isfile(imageName)):
			print("File exists")
			fp = open(imageName,"rb")
			imageName = MIMEImage(fp.read())
			fp.close()
			message.attach(imageName)
		else:
			print("Could not find image with the name :",imageName)
	else:
		print("No attachment")
	

	message["Subject"] = subject
	message["From"] = myEmail
	message["To"] = ", ".join(contacts)
	message.attach(MIMEText(myMessage))


	server = smtplib.SMTP("smtp.gmail.com",587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(myEmail,myPass)
	server.send_message(message)
	server.quit()

	print("Done 2")
