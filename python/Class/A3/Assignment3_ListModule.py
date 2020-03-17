def acceptNumber():
	
	numberOfElements = int(input("Number Of Elements: "))
	aList = list(map(int,input("\nEnter The Numbers: ").strip().split()))
	if(len(aList) != numberOfElements):
		print("Elements are not matching")
		exit()
	return aList

