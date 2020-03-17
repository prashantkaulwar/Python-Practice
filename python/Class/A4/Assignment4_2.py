import Assignment4_ListModule as a

def multiplicationUsingLambda(num1 , num2):
	return lambda x : num1 * num2



def main():
	aList = a.acceptNumber()
	x = multiplicationUsingLambda(aList[0],aList[1])
	print("Multiplication of %d and %d: " % (aList[0],aList[1]),x(0))

if __name__ == "__main__":
	main()
