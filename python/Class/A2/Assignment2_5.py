
def primeNumber(num):
	sum = 1; 
	
	for x in range(2,int((num/2)+1)):
		if(num%x == 0):
			sum = sum + x
	return "Not Prime" if sum > 1 else "Prime"


def main():
	print("Number is ",primeNumber(int(input("Enter Number: "))))
	

if __name__ == "__main__":
	main()
