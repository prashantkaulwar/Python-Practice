import threading
from time import *
import os
from sys import *

def func(name,val):
	name(val)

def small(string):
	print("Small Thread Name: ",threading.currentThread().getName())
	print("Thread ID: ",threading.currentThread().ident)
	smallsum = 0
	for x in string:
		if(x.islower()):
			smallsum += 1
	print("Number of small charector",smallsum)
	print()


def capital(string):
	print("Capital Thread Name: ",threading.currentThread().getName())
	print("Thread ID: ",threading.currentThread().ident)
	capsum = 0
	for x in string:
		if(x.isupper()):
			capsum += 1
	print("Number of Capital charector",capsum)
	print()

def digits(string):
	print("Digit Thread Name: ",threading.currentThread().getName())
	print("Thread ID: ",threading.currentThread().ident)
	numberofdigits = 0
	for x in string:
		if(x.isnumeric()):
			numberofdigits += 1
	print("Number of Capital charector",numberofdigits)
	print()

def main():
	v = input("Enter String: ")

	t1 = threading.Thread(target = func, args = (small,v,))
	t2 = threading.Thread(target = func, args = (capital,v,))
	t3 = threading.Thread(target = func, args = (digits,v,))

	t1.start()
	t2.start()
	t3.start()
	
	t1.join()
	t2.join()
	t3.join()
	
	print("Exit from Main()")

if __name__ == "__main__":
	main()

