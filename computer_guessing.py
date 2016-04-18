import random

def main():
	guesses = []
	try:
		secret_num = int(input("Enter a secret number between 1 to 100 "))
	except ValueError:
		print("Enter a number  ")
	else:
		a,b = 1,100
		while len(guesses) < 9:
			input()
			guess = random.randint(a,b)
			if guess == secret_num:
				print('you got it right the number is {} '.format(secret_num))
				break
			elif guess < secret_num:
				print('the number is greater then {}'.format(guess))
				a = guess + 1
			else:
				print('the number is less then {}'.format(guess))
				b = guess - 1
			guesses.append(guess)
		else:
			print("you didn't get it the number is {}".format(secret_num))
	a = input("do you want to continue Y/n  ")
	if a != 'n':
		main()
	else:
		print("Hope you njoyed the game see you soon")
main()


