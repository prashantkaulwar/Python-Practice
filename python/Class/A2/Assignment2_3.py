
def fact(num):
	return 1 if(num==1 or num==0)else num * fact(num-1)

def main():
	print(fact(int(input("Enter Number For Factorial: "))))
	

if __name__ == "__main__":
	main()
