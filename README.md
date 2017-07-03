## A gmail bot that is capable to sent the same email to many recipients

> The idea of this project was born when I had to send a notification email for a local chess tournament


** Requirements **
Python 3 
A gmail address (I recommend to create a new one and not use your personal address)


** How to get it up and running **
Edit the keys.py file by adding your credentials in the definded variables
```
myGmail = "-----"
myPass = "-----"
```
Create two files, one called *msg.txt* and one called *contacts.txt*
In *msg.txt* you can add the body of your email and in *contacts.txt* the email addresses of all the recipients one after the other in a new line

*If you do not create these two files, the program will create them for you but they will be empty*

**Be aware the program _does not check if the email address are valid_ it is up to you **


##Features that will be added in the future -Option to add an image -Option to send the email on specific date and time
