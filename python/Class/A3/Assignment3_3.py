def acceptNumber():
	
	numberOfElements = int(input("Number Of Elements: "))
	aList = list(map(int,input("\nEnter The Numbers: ").strip().split()))
	if(len(aList) != numberOfElements):
		print("Elements are not matching")
		exit()
	return aList

def findMinUsingInBuildFunction(aList):
	return min(aList)

def findMinWithoutUsingInBuildFunction(aList):
	minValue = aList[0]
	for x in aList:
		if(x < minValue):
			minValue = x
	return minValue

def main():
	aList = acceptNumber();
	minNumber = findMinUsingInBuildFunction(aList);
	print("Min Number Using In-Build Function is: ",minNumber)
	minNumber = findMinWithoutUsingInBuildFunction(aList);
	print("Min Number Without Using In-Build Function is: ",minNumber)

if __name__ == "__main__":
	main()
