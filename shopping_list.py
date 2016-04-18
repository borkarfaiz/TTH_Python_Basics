def show(items):
	print("the items which is currently on your cart is  ")
	for item in items:
		print(item)

def help():
	print(""" Type 'DONE' to quit
	'SHOW' to show the items
	'HELP' to get the help.""")

shopping_list = []
print("Enter the items")
help()

while True:
	item = input("-> ")
	if item == 'DONE':
		break
	elif item == 'SHOW':
		show(shopping_list)
	elif item == 'HELP':
		help()
	else:
		shopping_list.append(item)

show(shopping_list)
