import random
a = [1,5,3,'cheetah',4.5]

#traversing through the lists

for i in range(len(a)):
	print(a[i])

#enumerate function returns two values first index and second items in list
for index,item in enumerate(a):
	print("Index -",index,"Items -",item)

print(random.choice(a))
print(random.shuffle(a))
print(a.index('cheetah'))
print('cheetah' in a)