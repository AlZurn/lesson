import random as r
x = {}
c = 0
res = 0
while True:
	if c < 5:
		name = input('NAMES: ')
		x[name] = r.randint(1,10)
		c += 1
	else:
		break
print(x)
for i in x.values():
	if i >=5:
		res = i
		for j in x:
			if x[j] == res:
				print(j)
for i in x:
	if i == '1':
		print(i, x[i])
