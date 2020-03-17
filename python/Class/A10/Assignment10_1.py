from sys import *
import os

def DirectoryWatcher(path, checkext):

	flag = os.path.isabs(path)
	if flag == False:
		path = os.path.abspath(path)

	exists = os.path.isdir(path)
	Counter = 1
	if exists:
		for foldername,subfoldername,filename in os.walk(path):
			for filen in filename:
				extention = filen.split(".")
				if(len(extention) > 1): #Reason for this because some time we get no extention for the file
					if extention[1] == checkext[1:]:	
						print("File ",Counter,": ",filen)
						Counter += 1

	else:
		print("Invalid Path")


def main():
	print("Into the Main Function")
	
	print("Application Name: " + argv[0])

	if(len(argv) != 3):
		print("Error: Invalid number of arguments.")
		exit()

	if(argv[1] == '-H') or (argv[1] == '-h'):
		print("This Script is used to travers specific directory")
		exit()

	if(argv[1] == '-U') or (argv[1] == '-u'):
		print("Usage: ApplicatrionName AbsolutePath_of_Directory")
		exit()

	try:
		DirectoryWatcher(argv[1],argv[2])
	except ValueError:
		print("Error: Invalid datatype of input")
	except Exception:
		print("Error: Invalid input",Exception.with_traceback())

	


if __name__ == "__main__":
	main()

