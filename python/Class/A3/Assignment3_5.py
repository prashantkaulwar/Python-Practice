import Assignment3_ListModule as a
import Assignment3_PrimeModule as p

def chkPrime(aList):
	dsum = 0
	for x in aList:
		if(p.primeNumber(x)):
			dsum = dsum + x
	return dsum


def main():
	aList = a.acceptNumber()
	chkPrimeNo = chkPrime(aList)
	print("Sum Of Prime Is: ",chkPrimeNo)

if __name__ == "__main__":
	main()
