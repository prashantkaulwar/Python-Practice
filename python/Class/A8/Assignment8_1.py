import threading
from time import *
import os

def func(name,val):
	name(val)

def Even(no):
	counter = 1
	for i in range(1,(no*2)+1):
		if(i % 2 == 0):
			print("Even : ",counter,") : ", i)
			counter += 1

def Odd(no):
	counter = 1
	for i in range(1,(no*2)+1):
		if(i % 2 != 0):
			print("Odd : ",counter,") : ", i)
			counter += 1

def main():
	v = 10
	t1 = threading.Thread(target = func, args = (Even,v,))
	t2 = threading.Thread(target = func, args = (Odd,v,))
	
	t1.start()
	t2.start()

if __name__ == "__main__":
	main()

