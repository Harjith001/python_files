import random

secret_number = random.randint(1,20)
user_guess = 0
for i in range(6):
	user_guess = int(input('Guess a number between 1 and 20 : '))

	if user_guess>secret_number:
		print("nigga balls")
	elif user_guess<secret_number:
		print("nibbi balls")
	else:
		print("nigga found")
