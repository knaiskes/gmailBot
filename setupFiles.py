import os.path

def lookFiles(fileName):
	# checks if a file exists, if it doesn't it creates it
	if(not os.path.isfile(fileName)):
		print("Creating file: ",fileName)
		open(fileName,"w")


