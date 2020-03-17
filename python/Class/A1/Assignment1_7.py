
def checkNum():
	num = int(input("Please Enter Number: "))
	if(num % 5 == 0):
		return True
	else:
		return False


def main():
	status = checkNum()
	print("Status is: ",status)

if __name__ == "__main__":
	main()
