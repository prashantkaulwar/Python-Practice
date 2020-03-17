import Assignment2_1_module as a

def main():
	num1 = int(input("Enter First Number: "))
	num2 = int(input("Enter Second Number: "))
	print("Addition: ", a.Add(num1,num2))
	print("Substraction: ", a.Sub(num2,num1))
	print("Multiplication: ", a.Mult(num1,num2))
	print("Division: ", a.Div(num1,num2))

if __name__ == "__main__":
	main()
