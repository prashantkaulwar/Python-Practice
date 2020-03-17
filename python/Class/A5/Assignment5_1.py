import Assignment_Accept_String as a

def stringReverse(string):
	return string[::-1]

def main():
	result = stringReverse(a.acceptString())
	print("Reverse String: ", result)

if __name__ == "__main__":
	main()
