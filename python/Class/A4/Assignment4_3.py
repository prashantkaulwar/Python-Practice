import Assignment4_ListModule as a
import functools 

def productUsingLambda(aList):
	return list(map(lambda x: x + 10, filter(lambda x : x>=70 and x<=90,aList)))



def main():
	#Input_List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
	#aList = Input_List
	#aList = a.acceptNumber()
	result = productUsingLambda(aList)
	print(functools.reduce(lambda x,y: x * y, result))

if __name__ == "__main__":
	main()
