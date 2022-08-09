name = input('Enter your name : ')
print("Name :",name)
print('Name with title :',name.title()) #default function title() it changes each starting letter of a word to caps and other letters are changed to lower case
print(name.upper())
print(name.lower())
print(name.strip()) #removes white spaces right and left of the string
print(name*3) #here the string is displayed n times
#connverting int to strings using str()
num = 90
print('number is '+str(num)) #Note + is used for concating string so you cant concate int and string here use ','

#formatted strings
#these allows us to include the variable in the string quotes itself like in c

s = f'This is my name : {name}'
print(s)
print(f'My name is {name}')