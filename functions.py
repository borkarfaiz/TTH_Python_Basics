def hows_the_parrot():
	print("He's pining for the fjords!")
hows_the_parrot()

def lumberjack(name):
	if name.lower() == 'faiz':
		print("Faiz's a lumber and he's awesome")
	else:
		print("{} sleps all night and {} talks in the mobile whole day".format(name, name))

lumberjack('salman')

def average(num1, num2):
	return (num1 + num2) / 2

print(average(3,6)) 