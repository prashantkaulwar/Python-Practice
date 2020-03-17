import Assignment_Accept_String as a

def removeCharectorFromWord(string,position):
	del string[position]
	return "".join(string)

def main():
	string = list(a.acceptString())
	charNumber = int(input("Position: "))	
	print("String: ", removeCharectorFromWord(string,charNumber-1))

if __name__ == "__main__":
	main()
