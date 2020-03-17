import Assignment_Accept_String as a

def calculateAsciiValueOfWord(string):
	dsum = cnt = 0
	for x in string:
		dsum = dsum + ord(x)
		cnt = cnt + 1
	return (dsum/cnt)

def main():
	string = list(a.acceptString())
	print("Average Of Ascii Value: ", calculateAsciiValueOfWord(string))

if __name__ == "__main__":
	main()
