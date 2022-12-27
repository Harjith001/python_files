import math
a = 'harjith'
print(a[::-1])
print(a[::2])
print(a[:-3])
print(a[-3:])
print(len(a))
print(sorted(a))
print(a.isalpha())
print(a.isalnum())
print(a.count('h'))
print(a.endswith('i'))
print(a.find('h',1))

i = [2,56,67,2,90,69]
print(sorted(i))
print(math.log10(i[0]))
print(math.factorial(i[0]))
print(list(dict.fromkeys(i)))
print(list(set(i)))#removing duplicates

print(0o76)

if(i[0] == 3):
	pass
else:
	print('True')


temp = ''
max=0
c = ['Cochin', 'Chennai','Bangalore']
for j in c:
	l = len(j)
	if(l>max):
		max = l
		temp = j
	else:
		continue

print(temp)

x = 'I dont know what to type'
print(x.split(' '))