from sys import *
import os

def DirectoryWatcher(path):
	flag = os.path.isabs(path)
	if flag == False:
		path = os.path.abspath(path)

	exists = os.path.isdir(path)
	
	if exists:
		for foldername,subfoldername,filename in os.walk(path):
			print("Current folder is: "+foldername)
			for subf in subfoldername:
				print("Sub Folder of "+ foldername+" is: "+subf)
			for filen in filename:
				print("File inside "+ foldername+" is: "+filen)
			print("")
	else:
		print("Invalid Path")


def main():
	print("Into the Main Function")
	
	print("Application Name: " + argv[0])

	if(len(argv) != 2):
		print("Error: Invalid number of arguments.")
		exit()

	if(argv[1] == '-H') or (argv[1] == '-h'):
		print("This Script is used to travers specific directory")
		exit()

	if(argv[1] == '-U') or (argv[1] == '-u'):
		print("Usage: ApplicatrionName AbsolutePath_of_Directory")
		exit()

	try:
		DirectoryWatcher(argv[1])
	except ValueError:
		print("Error: Invalid datatype of input")
	except Exception:
		print("Error: Invalid input")

	


if __name__ == "__main__":
	main()

