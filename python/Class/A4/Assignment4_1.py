def testfunc(num):
	return lambda num : num * num



def main():
	number = int(input("Please Enter Number: "))
	n = testfunc(number)
	print("Squre Number: ",n(number))

if __name__ == "__main__":
	main()
