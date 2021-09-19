# def about_me(name, age):
# 		text = f'my name is {name}, I am {age} years old '
# 		print(text)
# name = input('What is your name? ')
# age = int(input('How old are you?' ))
# about_me(name, age) 
# def about_me(name, age): # >> name and age are arguments
# text = f”my name is {name}, I am {age} years old ”
# print(text)
# name = input(“What is your name? ”)
# age = int(input(“How old are you? ”))
# about_me(name, age) 
# def number(n):
# 	print( n**2 )

# x = number(5)
# print(x)
# def num(text):
# 	while True:
# 		name = input(text)
# 		if name.isdigit():
# 			x = int(name)
# 			return x
# 		else:
# 			print('vvedice cifru')
# a = num('asd')
# print(a)
# def vib():
# 	y = ('*','/','+','-')
# 	while True:
# 		name1 = input(' :')
# 		if name1 in y:
# 			return name1
			
# 		else:
# 			print('VVEDITE */-+')

# def res():
# 	z = num('number one ')
# 	c = vib() 
# 	y = num('number two ')
# 	if c == '+':
# 		return z + y 
# 	elif c == '-':
# 		return z - y
# 	elif c == '*':
# 		return z * y 
# 	elif c == '/':
# 		return z / y 
# print(res())	


# def friends(*args,**kwargs):
# 	print(type(args), args,kwargs)
# def info_friend(**kwargs):
# 	print(type(kwargs), kwargs)
# friends('Alex','Bob', 'Same',c ='asdasds')
# info_friend(name = 'Bob', age = 21, car = 'Bmw')
# def test(x):
# 	return x ** 2
# print(list(map(test, range(1,10))))
from functools import reduce
def add(x,y):
	c = x * y
	res = f'{x} * {y} = {c}'
	print(res)
	return c
print (add,[1,2,3,4,5])
# test = list(filter(lambda x: x % 2 == 0, range(10)))
# print(test)
