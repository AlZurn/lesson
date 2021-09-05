students = {'A': 5,'B': 3,'C': 5,'D': 2,'E': 6,'C': 7}
res = 0
for j in students.values():
	if res < j:
		res = j
c = res
for i in students:
	if students[i] == res:
		print(i)
# for i in students.values():
# 	if i < c:
# # 		c = i 
# # print(c)
# # print(res)
# # # for i in range(c,res,c):
# # # 	if res % i == 0 and c % i ==0:
# # # 		print(i)
# # # 	else:
# # # 		print('chka')
# # # d = (res + c) / 2
# # # print(d)
# # for i in students.values():
# # 	res += i 
# # print(res/len(students.keys()))
# # res = list(range(1,5))
# # print(res)

# students = {'Aram': 5,'B': 3,'C': 5,'D': 2,'E': 6,'C': 7}
# res = 0
# c = 0
# for j in students.values():
# 	if res < j:
# 		res = j
# for i in students.keys():
# 	if students[i] == res:
# 		print(i)
# # for j in students.values():
# # 	if j > c and j < res:
# # 		c = j
# # for i in students.keys():
# # 	if students[i] == c:
# # 		print(i)
# c = sorted(students.values())[-2:]
# print(c)
# c = ''
# for i in students.keys():
# 	if i == 'Aram':
# 		del students[i]
# 		break
# else:
# 	print('No')
# print(students)
# if c == 'YES':
# 	del students['Aram']
# print(students)
# else:
# 	print('CHKA')
res = 0
students = {'Aram': 7,'B': 3,'C': 5,'D': 2,'E': 6,'C': 7}
for i in students.values():
	if res <= i and i > 6:
		res = i

for i in students.keys():
	if students[i] == res:
		print(i)