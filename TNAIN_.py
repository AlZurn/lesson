# a = ['a',2,'b',3,'c',5,'j',6,'d',8]
# b = {}
# for i in range(0,len(a),2):
# 	b[a[i]] = a[i+1]

# print(b)
# # ynchi chem krna res += 1 harcEEEEEEEEEEER

# a = ['a',2,'b',3,'c',5,'j',6,'d',8,'a',9,'a',4]
# res = {}
# num = []
# alf = []
# for i in a:
# 	i = str(i)
# 	if i.isalpha():
# 		alf.append(i)
# 	else:
# 		num.append(i)

# for i,j in zip(alf,num):
# 	if i not in res:
# 		res[i] = j
# 	else:
# 		c = int(res[i]) + int(j)
# 		res[i] = c
# print(res)
# es megy erelem zorov sharov bayc imenno primer chem krna jogem or luboy bani exni, ete tar u tiv chexni irar hedevic grac inchx bdi enem

## ELI HARC UNIM 
# word = 'exercises'
# l = list(word)
# a = {}
# res = 0
# for i in l:
# 	if i is not ( not in )  a:
# 		a[i] = l.count(i)
# 	# 	a[i] = 1
# 	# else:
# 	# 	a[i] = 5 BDI HARCNEM TE YNCHI CHI ASHXADI ELSEN
# print(a)

old_list = [{'key1':'value1'},{},{},{},{'key1':'value1'},{'key2':'value2'}]

for i in old_list:
	if old_list.count(i) > 1:
		old_list.remove(i)
print(old_list)




