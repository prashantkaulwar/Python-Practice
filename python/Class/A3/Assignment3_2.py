def acceptNumber():
	
	numberOfElements = int(input("Number Of Elements: "))
	aList = list(map(int,input("\nEnter The Numbers: ").strip().split()))
	if(len(aList) != numberOfElements):
		print("Elements are not matching")
		exit()
	return aList

def findMaxUsingInBuildFunction(aList):
	return max(aList)

def findMaxWithoutUsingInBuildFunction(aList):
	maxValue = 0
	for x in aList:
		if(x > maxValue):
			maxValue = x
	return maxValue

def main():
	aList = acceptNumber();
	maxNumber = findMaxUsingInBuildFunction(aList);
	print("Max Number Using In-Build Function is: ",maxNumber)
	maxNumber = findMaxWithoutUsingInBuildFunction(aList);
	print("Max Number Without Using In-Build Function is: ",maxNumber)

if __name__ == "__main__":
	main()
