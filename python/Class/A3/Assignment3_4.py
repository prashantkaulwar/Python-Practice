def acceptNumber():
	
	numberOfElements = int(input("Number Of Elements: "))
	aList = list(map(int,input("\nEnter The Numbers: ").strip().split()))
	if(len(aList) != numberOfElements):
		print("Elements are not matching")
		exit()
	return aList

def findFrequency(aList):
	number = int(input("Please Enter Number: "))
	cnt = 0
	for x in aList:
		if(x == number):
			cnt = cnt + 1
	return cnt


def main():
	aList = acceptNumber()
	frequency = findFrequency(aList)
	print("Frequency is: ",frequency)

if __name__ == "__main__":
	main()
