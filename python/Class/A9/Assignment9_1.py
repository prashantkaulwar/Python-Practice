from sys import *
import os

def CheckFileExistsOrNot(filename):
	exists = os.path.isfile(filename)
	if(exists):
		print("File is exists")
	else:
		print("Files does not exists")

def main():
	print("Into the Main Function")
	
	print("Application Name: " + argv[0])

	if(len(argv) != 2):
		print("Error: Invalid number of arguments.")
		exit()
	if(argv[1] == '-H') or (argv[1] == '-h'):
		print("This Script is used to check the files is exist or not")
	if(argv[1] == '-U') or (argv[1] == '-u'):
		print("Usage: ApplicatrionName AbsolutePath_of_Directory")
		exit()

	try:
		CheckFileExistsOrNot(argv[1])
	except ValueError:
		print("Error: Invalid datatype of input")
	except Exception:
		print("Error: Invalid input")

	


if __name__ == "__main__":
	main()

