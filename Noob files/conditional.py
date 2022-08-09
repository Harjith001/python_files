# colon is used instead of curly brackets
age = int(input('Enter your age for verification : '))
if(age >=18):
	print('You are completely not eligible for kids playground')
elif(age==17):    
	print('I will give you a pass')
else:
	print("You are eligible for kids playground!")