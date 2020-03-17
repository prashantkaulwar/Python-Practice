
def NumState(num):
	if num == 0:
		print("Zero")
	elif num < 0:
		print("Negative Number")
	else:
		print("Positive Number")


def main():
	NumState(int(input("Please Enter Number")))

if __name__ == "__main__":
	main()
