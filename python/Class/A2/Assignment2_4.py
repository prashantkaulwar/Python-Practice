
def numFactorAddition(num):
	sum = 1;
	print(sum,sep= " + ")
	for x in range(2,int((num/2)+1)):
		if(num%x == 0):
			print(x,sep= " + ")
			sum = sum + x
	return sum


def main():
	print("Addition of its factors: ",numFactorAddition(int(input("Enter Number Addtions of Factors: "))))
	print("")
	

if __name__ == "__main__":
	main()
