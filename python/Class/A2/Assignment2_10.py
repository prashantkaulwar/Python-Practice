
def SumOfDigit(num):
	if(num <= 0):
		return 0;
	else:
		abc = num % 10
		num = int(num / 10)
		return abc + SumOfDigit(num)
		

def main():
	dsum = SumOfDigit(int(input("Please Enter Number For Digit Length By Int: ")))
	print("Sum Of Digit ",dsum)
	

if __name__ == "__main__":
	main()
