import random
import sys
#To play rock paper scissor with computer using random function
user_choice = ''
while True:
	print('Welcome nigga to rock paper scissor game')
	print('Enter your choice \nEnter r for rock\nEnter p for paper\nEnter s for scissor')
	while True:
		user_choice = input()
		if user_choice == 'r' or user_choice == 'p' or user_choice == 's':
			break
		else:
			print('Enter a valid choice u nigga')

	temp = random.randint(0,2)
	computer_choice = ''
	if temp == 0:
		computer_choice = 'r'
	elif temp == 1:
		computer_choice = 'p'
	elif temp == 2 :
		computer_choice = 's'
	else:
		print('random value is out of boundsb')
	#checking for game conditions

	if computer_choice == user_choice:
		print('Nigga u and computer have same choice so Draw')
	elif computer_choice == 'r' and user_choice == 's':
		print('Computer choice is',computer_choice,'\nUser choice is ',user_choice,'\n Nigga you lose')
	elif computer_choice == 'p' and user_choice == 'r':
		print('Computer choice is',computer_choice,'\nUser choice is ',user_choice,'\n Nigga you lose')
	elif computer_choice == 's' and user_choice == 'p':
		print('Computer choice is',computer_choice,'\nUser choice is ',user_choice,'\n Nigga you lose')
	elif user_choice == 'r' and computer_choice == 's':
		print('Computer choice is',computer_choice,'\nUser choice is ',user_choice,'\n Nigga you Win')
	elif user_choice == 's' and computer_choice == 'p':
		print('Computer choice is',computer_choice,'\nUser choice is ',user_choice,'\n Nigga you Win')
	elif user_choice == 'p' and computer_choice == 'r':
		print('Computer choice is',computer_choice,'\nUser choice is ',user_choice,'\n Nigga you Win')

	temp = int(input('Enter 1 to continue : '))
	if temp == 1:
		continue
	else:
		sys.exit(1)