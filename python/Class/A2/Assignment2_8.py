
def printPattern(num):
	for y in range(1,(num+1)):
		for x in range(1,(y+1)):
			print(x, end=" ")
		print("")

def main():
	printPattern(int(input("Please Enter Number: ")))
	

if __name__ == "__main__":
	main()
