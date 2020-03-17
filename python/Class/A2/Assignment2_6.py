
def printPattern(num):
	for y in range(num,0,-1):
		for x in range(y,0,-1):
			print("*", end=" ")
		print("")

def main():
	printPattern(int(input("Please Enter Number: ")))
	

if __name__ == "__main__":
	main()
