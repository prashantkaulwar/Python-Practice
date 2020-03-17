import threading

amount = 0

def Counter(fun,lock):
	fun(lock)

def Credit(lock):
	value = int(input("Enter Amount to Credit : "))
	lock.acquire()
	global amount
	amount += value
	print("Balance Amount is ",amount)
	print()
	lock.release()

def Debit(lock):
	value = int(input("Enter Amount to Debit : "))
	lock.acquire()
	global amount
	if amount < value:
		print("Unable to withdraw")
		print()
	else:
		amount += value
		print("Amount Withdraw ",value)
		print("Balance Amount ", amount)
		print()
	lock.release()

def main():
	lock = threading.Lock()

	t1 = threading.Thread(target = Counter, args = (Credit,lock,))
	t2 = threading.Thread(target = Counter, args = (Debit,lock,))

	t1.start()
	t2.start()

	t1.join()
	t2.join()

if __name__ == "__main__":
	main()

