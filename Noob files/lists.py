#lists are like arrays to store multiply values
num = [1,2,3,4,5]
print(num) #printd the whole list with brackets
print(num[0])

x =[4,5,6,7,8];
print(x[-1]) #to print the elements from last of the list

#lists are dynamic so you can add or remove elements from a list
num.append(6)
print(num)

name = [] #creating an empty list and adding elements
name.append('Pikachu')
name.append('Charizard')
name.append('Blastose')
print(name)

#inserting elements in a list
name.insert(0,'Bulbasore')
print('Name after inserting\n',name)

#removing elements from lists
del name[0]
print('After removing\n',name)
print('Popped element :',name.pop()) #element will be popped and returns the element,defaultly nut you can enter a index for pop()
print(name)

#removing an element by value
name.remove('Charizard')
print(name)

n=[5,4,8,1,3,2]
n.sort() #to sort the elements in list also works with string
print(n)
n.sort(reverse=True)
print(n) #sorts in descending order

#in .sort() it changes the original string
#if you need to temporarily sort it then use sorted()
print(sorted(n))

print(len(n))