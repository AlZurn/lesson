import random as r

def start():
	global name
	print('                    YOU PLAY BLOT ')
	name = input('                   WHAT IS YOUR NAME ?  ')

start()

def card():

	all_cards = []
	cards_type = [ 'CLUB ♣', 'DIAMOND ♦', 'HEART ♥', 'SPADE ♠' ]
	cards =      [ 9, 10, 'J', 'Q', 'K', 'T' ] 

	for i in cards_type:
		for j in cards:
			result = i + str(j)	 
			all_cards.append(result)
			
	r.shuffle(all_cards)

	player = []
	comp = []

	for  i in range(5):
		players_card = all_cards.pop()
		player.append(players_card)
		comp_cards = all_cards.pop()
		comp.append(comp_cards)

	trump_card = all_cards.pop()

	player.sort()
	comp.sort()	

	print('')
	print('TRUMP CARD -    ',trump_card)
	print('')
	print(name, player)
	print('')
	print('COMP ',comp)
	print('')
	print('           ',name)

	while True:
		player_choice = input('             YOU WANT TO TAKE TRUMP CARD yes(y) , (no):  ') == 'y'

		if player_choice:
			player.append(trump_card)
			for i in range(2):
				playees_card = all_cards.pop()
				player.append(playees_card)

			for i in range(3):	
				comp_cards = all_cards.pop()
				comp.append(comp_cards)
			break
		
		if 'J' in trump_card:

			comp.append(trump_card)
			for i in range(1,4):
				playees_card = all_cards.pop()
				player.append(playees_card)

			for i in range(1,3):	
				comp_cards = all_cards.pop()
				comp.append(comp_cards)
			break

		print("")
		print('            COMP')
		comp_choice = input('             YOU WANT TO TAKE TRUMP CARD yes(y) , (no):  ') == 'y'		
		
			
		if comp_choice:
			comp.append(trump_card)
			
			for i in range(3):
				playees_card = all_cards.pop()
				player.append(playees_card)


			for i in range(2):	
				comp_cards = all_cards.pop()
				comp.append(comp_cards)
			break		
	
		else:
			cards_type_new = ['CLUB', 'DIAMOND', 'HEART', 'SPADE','NOTTYPE' ]

			print('')
			print('           ',name)
			change_trump_player = input('             WHAT YOU WANT TO TAKE/ CLUB ♣, DIAMOND ♦, HEART ♥, SPADE ♠, NOTTYPE / OR (NO):  ' )		
			z = change_trump_player.upper()

			if z in cards_type_new:
				print('')
				print('           ',name)
				print('           TRUMP CARD -    ',trump_card)
				player_choice = input('             YOU WANT TO TAKE TRUMP CARD yes(y) , (no):  ') == 'y'
				
				if player_choice:
					player.append(trump_card)
			
					for i in range(1,3):
						playees_card = all_cards.pop()
						player.append(playees_card)			
					
					for i in range(1,4):	
						comp_cards = all_cards.pop()
						comp.append(comp_cards)
					break		
				else:
					
					for i in range(1,4):
						playees_card = all_cards.pop()
						player.append(playees_card)			
					
					for i in range(1,4):	
						comp_cards = all_cards.pop()
						comp.append(comp_cards)	
					break		
			else:
			
				while True:

					print("")
					print('            COMP')
					chenage_trump_comp = input('             WHAT YOU WANT TO TAKE/ CLUB ♣, DIAMOND ♦, HEART ♥, SPADE ♠, NOTTYPE :  ' )				
					x = chenage_trump_comp.upper()

					if x in cards_type_new:
						print("")
						print('            COMP')
						print('            TRUMP CARD -    ',trump_card)
						comp_choice = input('             YOU WANT TO TAKE TRUMP CARD yes(y) , (no):  ' ) == 'y'

						if comp_choice:
							comp.append(trump_card)
							for i in range(1,3):	
								comp_cards = all_cards.pop()
								comp.append(comp_cards)

							for i in range(1,4):
								playees_card = all_cards.pop()
								player.append(playees_card)	
							break
						else:
					
							for i in range(1,4):
								comp_cards = all_cards.pop()
								comp.append(comp_cards)			
					
							for i in range(1,4):	
								playees_card = all_cards.pop()
								player.append(playees_card)	
							break						
		break			

	player.sort()
	comp.sort()	
	# point = 0
	# for i in player:
	# 	if "J" in i:
	# 		point += 2
	# 	elif 'Q' in i:
	# 		point += 3` 
	# 	elif 'K' in i: 
	# 		point += 4
	# 	elif 'T' in i:
	# 		point += 11
	# 	elif '9' in i:
	# 		point += 14
	# 	elif '10' in i:
	# 		point += 10					

	print('')		
	print(name, player)
	print('')
	print('COMP',comp)

		
card()