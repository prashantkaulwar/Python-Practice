import Assignment4_ListModule as a
import functools 

def primeNumber(num):
	sum = 1; 
	
	for x in range(2,int((num/2)+1)):
		if(num%x == 0):
			sum = sum + x
	return 0 if sum > 1 else num

def eventNumberSqureUsingLambda(aList):
	return list(map(lambda x: x * 2, filter(lambda x : primeNumber(x),aList)))



def main():
	#Input_List = [2, 70 , 11, 10, 17, 23, 31, 77]
	#aList = Input_List
	aList = a.acceptNumber()
	result = eventNumberSqureUsingLambda(aList)
	print(functools.reduce(lambda x, y: x if (x > y) else y, result))

if __name__ == "__main__":
	main()
