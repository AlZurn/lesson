# l = [1,3,5,1,5,15,12,12]

# try:
# 	print(l[11])
# except IndexError:
# 	print('x ne sushestvuet')
# m = {'0a': 3}
# try:
# 	print(m['a'])
# except KeyError:
# 	print('x ne sushestvuet')

# try:
# 	num1 = int(input('1 : '))
# 	num2 = int(input('2 : '))
# 	print(num1/num2)
# except ZeroDivisionError:
# 	print('Na 0 / nelzya')
# except ValueError:
# 	print('vveite cifru')


	# x = input('Name :')
	# if x.isdigit():
	# 	raise TypeError('VVEDITE NE CIFRU')
	# break
	# except TypeError as E:
	# 	print(E)
	# try:
	# 	x = input('ALEX: ')
	# except KeyboardInterrupt:
	# 	print('asdasd')
# try:
# 	print('barev' + 5)
# except TypeError:
# 	print('STR INT')




# try:
# 	print("Hello")
# except:
# 	print("Something went wrong")
# else:
#  	print("Nothing went wrong")


# try:
# 	print(x)
# except (NameError, TypeError):
# 	print("Something went wrong")
# finally:
# 	print("The 'try except' is finished")

# try:
# 	x = int(input('AGE :' ))
# 	if x < 0:
# 		raise ValueError('NELZYA')
# except ValueError as R:
# 	print(R)

# test = 'Python'
# # iterable_test = iter(test)
# # while True:
# # 	try:
# # 		item = next(iterable_test)
# # 		print(item)
# # 	# except StopIteration:

# # 		break
# x = iter(test)
# print(next(x))
# print(next(x)) 
# print(next(x)) 
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))


# age = "hello"
# if isinstance(age, str):
# 	raise TypeError("Only integers are allowed")


# def test(mylist):

# 	assert len(mylist) != 0
# 	return sum(mylist)/len(mylist)

# mylist = [5]

# try:
# 	print("Average of mylist:",test(mylist))
# except AssertionError:
# 	print('asd')
# while True:
	
# 	try:
# 		x = input('VVEDITE PAROL: ')
# 		if len(x) <= 6:
# 			raise ValueError('VVEDITE PAROL dlinoy 6 ')
# 		else:
# 			break
# 	except ValueError as V:
# 		print(V)

# a = 5
# b = 2
# a = a + b
# b = a - b
# a = a - b 
# print(a,b)