import os
import bs4
import requests
import webbrowser
from sys import *

def openurl(url,count):
	for x in range(0,count):
		connection = webbrowser.open(url)


def main():
	print("In Main")
	
	if(len(argv) != 3):
		print("Error: Invalid number of arguments.")
		exit()

	if(argv[1] == '-H') or (argv[1] == '-h'):
		print("This Script is used to open a given url into the browser")
		exit()

	if(argv[1] == '-U') or (argv[1] == '-u'):
		print("Usage: URL NumberOfTimeURLShouldOpen")
		exit()

	try:
		count = int(argv[2])
		openurl(argv[1],count)
	except ValueError:
		print("Error: Invalid datatype of input",ValueError.with_traceback())
	except Exception:
		print("Error: Invalid input",Exception.with_traceback())

	


if __name__ == "__main__":
	main()


