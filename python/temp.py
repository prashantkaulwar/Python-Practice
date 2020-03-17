'''
num1 = int(input('Please enter 1st number'))
num2 = int(input('Please enter 2nd number'))


sum = num1 + num2

print("Sum of {0} and {1} is {2}".format(num1, num2, sum))


def factorial(n):
	print("{0},".format(n))
	return 1 if(n==1 or n==0)else n * factorial (n-1)

num = int(input('Enter Number: '))
fact = factorial(num);
print("Factorial of {0} is {1}". format(num, fact))'''

a = ('1',['a','s','f','w','q'],'76567','asdgh')
print(a)
l1 = ['a','2','a','a','a']
a[1] = (['a','s','f'])
print(a)
