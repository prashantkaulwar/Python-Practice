import threading

def func(name,lock):
	name(lock)

def Thread1(lock):
	lock.acquire()
	for x in range(0,50):
		print("Thread1",x)
	lock.release()


def Thread2(lock):
	lock.acquire()
	for x in range(50,0,-1):
		print("Thread2",x)
	lock.release()

def main():
	lock = threading.Lock()

	t1 = threading.Thread(target = func, args = (Thread1,lock,))
	t2 = threading.Thread(target = func, args = (Thread2,lock,))

	t1.start()
	t2.start()
	
	t1.join()
	t2.join()
	
	print("Exit from Main()")

if __name__ == "__main__":
	main()


#asdasdasd
'''
asdhgbhd
a;skdjsadsdhasyudg
alsdhasd
aslkjd
sadj

'''

print(a)

"""kjsadhjashd
saduhaskhd
aslkdhksadh
skladjlk
"""
print(a)

