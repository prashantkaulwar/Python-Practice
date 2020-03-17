
def findLengthOfDigitUsingStr(num):
	print("Count is ",len(num))

def findLengthOfDigitUsingInt(num,count):
	while(num > 0):
		abc = num % 10
		num = int(num / 10)
		count = count + 1
		findLengthOfDigitUsingInt(num, count)	
	
	return count

def main():
	findLengthOfDigitUsingStr(str(input("Please Enter Number For Digit Length By String: ")))
	count = findLengthOfDigitUsingInt(int(input("Please Enter Number For Digit Length By Number: ")),0)
	print("Count is ",count)
	

if __name__ == "__main__":
	main()
