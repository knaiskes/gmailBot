from setupFiles import *
from sendEmail import *
from keys import *

lookFiles("msg.txt")
lookFiles("contacts.txt")

print("Enter email's subject:")
subject = input()


sendEmail(myGmail,myPass,subject)
