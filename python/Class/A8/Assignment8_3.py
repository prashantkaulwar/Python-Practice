import threading
from time import *
import os
from sys import *

def func(name,val):
	name(val)

def EvenList(num):
	Even_sum = 0;
	for x in range(0,len(num)):
		if(int(num[x])%2 == 0):
			Even_sum = Even_sum + int(num[x])
	print("Sum of Even Number ",Even_sum)


def OddList(num):
	Odd_sum = 0;
	for x in range(0,len(num)):
		if(int(num[x])%2 == 1):
			Odd_sum = Odd_sum + int(num[x])
	print("Sum of Odd Number ",Odd_sum)

def main():
	v = input("Enter List on Interger for list adding space").split()

	t1 = threading.Thread(target = func, args = (EvenList,v,))
	t2 = threading.Thread(target = func, args = (OddList,v,))

	t1.start()
	t2.start()
	
	t1.join()
	t2.join()
	print("Exit from Main()")

if __name__ == "__main__":
	main()

