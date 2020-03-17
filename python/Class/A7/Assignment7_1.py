
class BookStore(object):
	NoOfBooks = 0 #value shared across all class instances

	def __init__(self,Name,Author):
		self.Name = Name #value specific to instance. Instance variables are usually initialized in methods
		self.Author = Author #value specific to instance. Instance variables are usually initialized in methods
		addBookCount()

	def Display(self):
		print(self.Name,self.Author,"Number Of Books: ",NoOfBooks)

def main():
	Obj1 = BookStore('Linux System Programming', 'Robert Love')
	Obj1.Display()
	Obj2 = BookStore('C Programming', 'Dennis Ritchie')
	Obj2.Display()


if __name__ == "__main__":
	main()

6360218
