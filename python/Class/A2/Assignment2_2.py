
def displayPattern(num):
	for x in range(0,num):
		for y in range(0,num):
			print("*",end=" ")
		print("")

def main():
	displayPattern(int(input("Enter Number For Pattern: ")))
	

if __name__ == "__main__":
	main()
