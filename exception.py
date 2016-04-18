try:
	number = int(input("Enter a Integer number  "))
except ValueError:
	print("That's not a number!")
else:
	print("Hey " * number)	