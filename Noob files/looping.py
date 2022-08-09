for i in range(5): #here i value starts from 1 and ends before 5 
	print(i) #it does not print 5

#using rang function to make a list of numbers
num = list(range(1,31))
print(num)

#range to skip numbers 
for i in range(2,11,2):
	print(i) #prints only even numbers 

#creating squares with loop
squares = []
for i in range(1,5):
	squares.append(i**2) #squaring numbers by using exponents
print(squares)

#simple default functions in numeric list
print(min(num))
print(sum(num))

#shorthand convention to make a numeric lists
cubes = [i**3 for i in range(1,7)]
print(cubes)

#slicing the list

print(cubes[1:4]) #slices till only 3 like range
print(cubes[2:])
print(cubes[-2:]) #negative value means prints last two elements