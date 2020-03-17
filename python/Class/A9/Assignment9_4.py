from sys import *
import os.path

def CompareFileContent(filename1,filename2):
	exists1 = os.path.isfile(filename1)
	exists2 = os.path.isfile(filename2)
	if(exists1) and (exists2):
		fileHandler1 = open(filename1,'r')
		fileContent1 = fileHandler1.read()
		fileHandler2 = open(filename2,'r')
		fileContent2 = fileHandler2.read()
		if(fileContent1 == fileContent2):
			print("Success");
		else:
			print("Failure")
	else:
		print("Files does not exists")

def main():
	print("Into the Main Function")
	
	print("Application Name: " + argv[0])

	if(len(argv) != 3):
		print("Error: Invalid number of arguments.")
		exit()
	if(argv[1] == '-H') or (argv[1] == '-h'):
		print("This Script is used to check the files is exist or not")
	if(argv[1] == '-U') or (argv[1] == '-u'):
		print("Usage: ApplicatrionName AbsolutePath_of_Directory")
		exit()

	try:
		CompareFileContent(argv[1],argv[2])
	except ValueError:
		print("Error: Invalid datatype of input")
	except Exception:
		print("Error: Invalid input")

	


if __name__ == "__main__":
	main()

