from threading import *
from multiprocessing import *
from time import *
from os import *

def Squre(no):
	print(os.getpid())
	return no * no

def main():
	arr = [1,31,41,3,5,4,2]
	brr= []

	starttime1 = time()
	for i in range(len(arr)):
		brr.append(Squre(arr[i]))
	endtime1 = time()

	print(brr)

	print("serial :",endtime1-starttime1)

	pobj = Pool()

	starttime2 = time()
	crr = pobj.map(Squre,arr)
	endtime2 = time()

	print(crr)

	print("Parllel",endtime2-starttime2)
	print(os.getpid())

if __name__ == "__main__":
	main()
