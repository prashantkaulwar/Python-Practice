from os import *
from sys import *
import shutil
import tempfile
import requests	
import json

def FindDetails(zipcode):
	url_str = "https://whoismyrepresentative.com/getall_mems.php?zip="
	url_str1 = "&output=json"

	response = requests.urlopen(url_str+zipcode+url_str1)
	#response = urllib.urlopen(req)
	#the_page = response.read()	
	#page_details = json.loads(the_page)
	#print(page_details)

def main():
	print("Into the Main Function")
	
	print("Application Name: " + argv[0])
	print(len(argv))
	if(len(argv) != 2):
		print("Error: Invalid number of arguments.")
		exit()

	if(argv[1] == '-H') or (argv[1] == '-h'):
		print("This Script is used to Get the information of senetor from its zip code")
		exit()

	if(argv[1] == '-U') or (argv[1] == '-u'):
		print("Usage: ApplicatrionName ZipCode")
		exit()

	try:
		FindDetails(argv[1])
	except ValueError:
		print("Error: Invalid datatype of input")
	except Exception:
		print("Error: Invalid input",Exception.with_traceback())
		

if __name__ == "__main__":
	main()
