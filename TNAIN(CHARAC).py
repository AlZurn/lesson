a = [9,5,8,7,4]
b = 2
count = 1
c = ''
while True:
	if c != 'y':
		for i in a:
			if i == b:
				print(i, '1 ISXOD')
				c = 'y'
	
	if c != 'y':
		for i in a:
			if b + count == i: 
				print(i, '2 ISXOD')
				c = 'y'
			else:
				if b - count == i:
					print(i, '2 MINUSOV')
					c = 'y'
	count += 1




	

