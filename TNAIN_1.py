import random as r 
res = 0
user = 0
cd = 0
kto = r.randint(1,2)
if kto == 1:
	print('Игру начинаете ВЫ')
	while True:
		if res < 21:
			while True:
				user = int(input('Введите число 1-3 : '))
				if user >= 0 and user <= 3:
					res += user
					print (res)
					if res >= 21:
						print('Вы проиграли')
						break
					break
				else:
					print('Ведите число от 1-3, не понятно что ли')
			if res < 21:
				cd = 4-user
				res += cd
				print(res)
				if res >=21:
					print('Компьютер проиграл')
		else:
			break
else:
	print('Певым начинает Компьютер')
	while True:
		if res < 21:
			if res == 0:
				res = r.randint(1,3)
				print(res) 
			# elif res < 4:
			# 	cd = 4-res
			# 	res += cd
			# 	print(res)
			# elif res > 4 and res < 8:
			# 	cd = 8-res
			# 	res += cd
			# 	print(res)
			# elif res > 8 and res < 12:
			# 	cd = 12-res
			# 	res += cd
			# 	print(res)
			# elif res > 12 and res < 16:
			# 	cd = 16-res
			# 	res += cd
			# 	print(res)
			elif res > 0: 
				cd = 4 - res%4
				print(cd)
			else:
				cd = 4-user
				res += cd
				print(res)
				if res >=21:
					print('Компьютер проиграл')
		while True:
			if res < 21:
				user = int(input('Введите число 1-3 : '))
				if user >= 0 and user <= 3:
					res += user
					print (res)
					if res >= 21:
						print('Вы проиграли')
						break
					break
				else:
					print('Ведите число от 1-3, не понятно что ли')
		else:
			break


