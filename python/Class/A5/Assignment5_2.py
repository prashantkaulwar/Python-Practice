import Assignment_Accept_String as a

def countNumberOfWords(string):
	return len(string.split(" "))

def main():
	result = countNumberOfWords(a.acceptString())
	print("Count Of String: ", result)

if __name__ == "__main__":
	main()
