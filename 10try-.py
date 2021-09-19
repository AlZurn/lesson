# def nulner(ip):
	
# 	return ip.replace('0','')
# ip = "216.008.094.196"

# print(nulner(ip))

# def tenis(results):
# 	player,comp,resplayer, compres = 0,0,0,0
# 	for i in results:
# 		if i == 'a':
# 			player += 1
# 		else:
# 			comp += 1 		
# 		if player >= 6 and player - comp > 1:
# 			resplayer += 1
# 			player = 0
# 		elif comp >= 6 and comp - player > 1:
# 			compres +=1
# 			comp = 0
# 	return f"player {resplayer} comp {compres}"
# results=['b','a','a','a','a','a','a','a','a','a','a','a','b','b','b','b','b','b',
# 'a','a','a','a','a','a','a','a','a','a','a','a','a','a','a']
# print(tenis(results))
# import datetime

# def maximus(l):
# 	# res = 0
# 	# for i in l:
# 	# 	if i >= res:
# 	# 		res = i
# 	return sorted(l)[-1]
	
# l = [1,3,5,1,5,2]
# c = datetime.datetime.now()

# print(maximus(l))
# print(datetime.datetime.now()-c)
import time 
from functools import wraps
# def time_test(func):
# 	@wraps(func) # use wraps to change name (even.__name__ )
# 	def times():
# 		start = time.time()
# 		func()
# 		print(time.time()-start)
# 	return times
# @time_test
# def even():
# 	even_list = []
# 	for number in range(10000000):
# 		if number % 2 == 0:
# 			even_list.append(number)
# print(even.__name__)





def test(func):
	def hello():
		print('hello')
		func()
	return hello
@test
def testme():
	print('Armen')
testme()

