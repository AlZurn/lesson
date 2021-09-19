import random 

print('\t\t\t\tHi you play Tic Tac Toe\n')

def print_tablo ():

	print('\n\n\t\t\t\t',all_steps[0],'|',all_steps[1],'|',all_steps[2])
	print('\t\t\t\t--- --- --- ')
	print('\t\t\t\t',all_steps[3],'|',all_steps[4],'|',all_steps[5])
	print('\t\t\t\t--- --- --- ')
	print('\t\t\t\t',all_steps[6],'|',all_steps[7],'|',all_steps[8],'\n\n')
	

def start():
	
	while True:
		global choice
		global steps
		global all_steps
		
		steps = []
		all_steps = [1,2,3,
			 		4,5,6,
			 		7,8,9]

		choice = input('\n\t\t\t\tYou want (X) or (O)  ').upper().strip()

		if choice in ("X","O"):
			break		
		else:
			print('\t\t\t\tYou dont input (X) or (O) ')


def player():
	
	while True:
		try:
			players_step = int(input('\n\t\t\t\tWhere you want write: '))

			if players_step in all_steps:	
				if players_step not in steps:
					steps.append(players_step)
					all_steps[players_step-1] = choice
					break
		except ValueError:
 			print("\t\t\t\tInput a correct number")		


def comp():

	while True:
		c = [i for i in all_steps if isinstance(i,int)]
		comp_step = random.choice(c)
		
		if comp_step not in steps:
			steps.append(comp_step)
			print("\t\t\t\tComp step",comp_step)
			if choice == 'X':	
				all_steps[comp_step-1] = 'O' 
			else:
				all_steps[comp_step-1] = 'X' 
			break

def game():
	
	while True:
		if len(steps) >= 5:
			if (all_steps[0] == all_steps[1] == all_steps[2] or
				all_steps[3] == all_steps[4] == all_steps[5] or
				all_steps[6] == all_steps[7] == all_steps[8] or
				all_steps[0] == all_steps[4] == all_steps[8] or		
				all_steps[2] == all_steps[4] == all_steps[6] or
				all_steps[0] == all_steps[3] == all_steps[6] or
				all_steps[1] == all_steps[4] == all_steps[7] or
				all_steps[2] == all_steps[5] == all_steps[8]):
				if all_steps.count('X') > all_steps.count('O'): 
					print(f'\t\t\t\tWin X  -',)
					break
				else:
					print(f'\t\t\t\tWin O  -',)
					break
						

			elif len(steps) == 9:
				print('\t\t\t\tNOBODY WIN')
				break	
			else:
				return True			

		else:
			return True	

def play ():
	start()
	print_tablo()
	
	while True:
		if choice == 'X':
			player()
			print_tablo()
			if not game():
				break
			comp()
			print_tablo()
			if not game():
				break
		
		else:
			comp()
			print_tablo()
			if not game():
				break	
			player()
			print_tablo()
			if not game():
				break
play()


def play_again():
	
	while True:
		answer  = input('\t\t\t\tYou want play again yes(y) or no? ')
		if answer.upper()=='Y':
			play()
		break	

play_again()