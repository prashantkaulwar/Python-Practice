import Assignment4_ListModule as a
import functools 

def eventNumberSqureUsingLambda(aList):
	return list(map(lambda x: x * x, filter(lambda x : x%2==0,aList)))



def main():
	Input_List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
	aList = Input_List
	#aList = a.acceptNumber()
	result = eventNumberSqureUsingLambda(aList)
	print(functools.reduce(lambda x,y: x + y, result))

if __name__ == "__main__":
	main()
