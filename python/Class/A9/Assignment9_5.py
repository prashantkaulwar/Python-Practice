from sys import *
import os.path

def frequencyFileContent(filename1,keyword):
	exists1 = os.path.isfile(filename1)
	counter = 0
	if(exists1):
		with open (filename1, 'rt') as myfile:    # Open lorem.txt for reading text.
			for myline in myfile:
				findedKeyword = False
				findedKeywordlen = myline.split()
				for key in findedKeywordlen:
					if (key == keyword):
						counter += 1
			
		if(counter):
			print("key Word Count is: ", counter);
		else:
			print("key Word Count is: 0");
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
		frequencyFileContent(argv[1],argv[2])
	except ValueError:
		print("Error: Invalid datatype of input")
	except Exception:
		print("Error: Invalid input")

	


if __name__ == "__main__":
	main()

