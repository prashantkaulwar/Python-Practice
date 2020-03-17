def primeNumber(num):
	prime = True; 	
	for x in range(2,int((num/2)+1)):
		if(num%x == 0):
			prime = False
			break

	return prime
