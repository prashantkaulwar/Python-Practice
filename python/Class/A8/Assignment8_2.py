import threading
from time import *
import os

def func(name,val):
	name(val)

def check_even(num):
	return True if(num%2 == 0) else False

def check_odd(num):
	return True if(num%2 == 1) else False

def Even(num):
	Even_sum = 0;
	for x in range(2,int((num/2)+1)):
		if(num%x == 0):
			is_x_even = check_even(x)
			if(is_x_even):
				Even_sum = Even_sum + x
	print("Sum of Even Factor is ",Even_sum)


def Odd(num):
	Odd_sum = 0;
	for x in range(1,int((num/2)+1)):
		if(num%x == 0):
			is_x_odd = check_odd(x)
			if(is_x_odd):
				Odd_sum = Odd_sum + x
	print("Sum of Odd Factor is ",Odd_sum)

def main():
	v = int(input("Pleaes enter Number: "))
	t1 = threading.Thread(target = func, args = (Even,v,))
	t2 = threading.Thread(target = func, args = (Odd,v,))
	
	t1.start()
	t2.start()

	t1.join()
	t2.join()
	
	print("Exit from Main()")

if __name__ == "__main__":
	main()

