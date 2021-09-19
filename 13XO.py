import random as r

def print_tablo ():

	print('\n\n\t\t\t\t',all_steps[0],'|',all_steps[1],'|',all_steps[2])
	print('\t\t\t\t--- --- --- ')
	print('\t\t\t\t',all_steps[3],'|',all_steps[4],'|',all_steps[5])
	print('\t\t\t\t--- --- --- ')
	print('\t\t\t\t',all_steps[6],'|',all_steps[7],'|',all_steps[8],'\n\n')
def start():
	global hashvarg
	global tex
	global all_steps
	global player
	player = input('Please input X or O: ')
	all_steps = [1,2,3,4,5,6,7,8,9]
	hashvarg = []

def nachalo():
	if player == 'X':
		while True:
			print('Игру начинаете вы')
			tex = int(input('1-9: '))
			if tex not in hashvarg:
				if tex in all_steps:
					hashvarg.append(tex)
					all_steps[tex-1] = 'X'
					break	
	else:
		while True:
			print('Начните игру')
			tex = int(input('1-9: '))
			if tex not in hashvarg:
				if tex in all_steps:
					hashvarg.append(tex)
					all_steps[tex-1] = 'O'
					break

def comp():
	
	if player == 'X':
		while True:
			tex = r.randint(1,9)
			if tex not in hashvarg:
				hashvarg.append(tex)
				all_steps[tex-1] = 'O'
				break
	else:
		while True:
			tex = r.randint(1,9)
			if tex not in hashvarg:
				hashvarg.append(tex)
				all_steps[tex-1] = 'X'
				break

def result():
	while True:
		if len(hashvarg) >= 5:
			if (all_steps[0] == all_steps[1] == all_steps[2] or
				all_steps[3] == all_steps[4] == all_steps[5] or
				all_steps[6] == all_steps[7] == all_steps[8] or
				all_steps[0] == all_steps[4] == all_steps[8] or		
				all_steps[2] == all_steps[4] == all_steps[6] or
				all_steps[0] == all_steps[3] == all_steps[6] or
				all_steps[1] == all_steps[4] == all_steps[7] or
				all_steps[2] == all_steps[5] == all_steps[8]):
				if all_steps.count('X') > 2: 
					print(f'\t\t\t\tWin X  -',)
					break
				elif all_steps.count('O') > 2:
					print(f'\t\t\t\tWin O  -',)
					break
						

			elif len(hashvarg) == 9:
				print('\t\t\t\tNOBODY WIN')
				
				break	
			else:
				return True			

		else:
			return True

start()
print_tablo()
while True:
	nachalo()
	print_tablo()
	if not result():
		break
	comp()
	print_tablo()
	if not result():
		break


	






