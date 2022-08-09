country = ['India','Switzerland','United Kingdom','United States']
print(len(country))
for name in country:  #here name is a variable so each iteration value of country[i] will be stored in name
	print(name) #loop executes till end of list so till list.len()

#copying a list  into another
a=[1,5,3,2,3]
b = a[:] #copying list a into b
print(a)
print(b)

#lists can store datas of different data types
h = [1,2,'harjith',8.90]
print(h)

#checking whether a list is empty

c = []
if c:
	print('List has elements')
else:
	print('List is empty')

toppings = ['mushroom','extra cheese','panneer','jalepenos','black olives']
requested_toppings =['mushroom','jalepenos','chicken']

for value in requested_toppings:
	if value in toppings: #'in'  checks whter the value is presentn in list or notn
		print('Yes we serve the topping')
	else:
		print('Sorry we dont serve the topping')