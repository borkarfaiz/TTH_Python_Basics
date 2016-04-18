import random

# generate a random number between 1 and 10
def main():
	secret_num = random.randint(1, 10)
	guesses = []
	while len(guesses) < 3:

		# get a number guess from a number
		try:
			guess = int(input("Guess a number betweem 1 to 10   "))
		except ValueError:
			print("{} is not a number")
			break
		# compare guess to secret number
		else:
			if guess == secret_num:
				print("You got it! right my number is  {}".format(secret_num))
				print("You Won !!!!!!!!!!!")
				break
			elif guess > secret_num:
				print("My number is Smaller then {}".format(guess))
			else:
				print("My number is greater then {}".format(guess))
			guesses.append(guess)
	
	else:
		print("You didn't get it my number was {}".format(secret_num))
	a = input("Press 'n' cancel  ")
	if a != 'n':
		main()
	else:
		print("If you njoyed please visit us again")
		print("By" + 'e' * 14)
main()