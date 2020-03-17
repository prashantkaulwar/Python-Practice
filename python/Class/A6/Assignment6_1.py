import Assignment_Accept_String as a

class Demo(object):
	tev = 1 #value shared across all class instances

	def __init__(self,instance_variable_value1):
		self.tev = instance_variable_value1 #value specific to instance. Instance variables are usually initialized in methods

	def fun():
		print(self.no1)
	def gun():
		print(self.no1)

def main():
	no1 = Demo("abc")
	no2 = Demo("CPE")
	
	no1.fun()
	no2.fun()
	no1.gun()
	no2.gun()	


if __name__ == "__main__":
	main()
