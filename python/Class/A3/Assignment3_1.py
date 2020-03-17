def acceptNumber():
	
	numberOfElements = int(input("Number Of Elements: "))
	aList = list(map(int,input("\nEnter The Numbers: ").strip().split()))
	if(len(aList) != numberOfElements):
		print("Elements are not matching")
		exit()
	return aList

def numberAddition(aList):
	nsum = 0
	for x in range(0,len(aList)):
		nsum = nsum + aList[x]
	return nsum

def main():
	aList = acceptNumber();
	aSum = numberAddition(aList);
	print(aSum)

if __name__ == "__main__":
	main()
