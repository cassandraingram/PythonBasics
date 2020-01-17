# calculator.py

# create a function called add
def add():
	a = 1
	b = 2
	c = a + b
	print("{} + {} = {}" .format(a, b, c))

def add2(x, y):
	z = x + y
	print("{} + {} = {}" .format(x, y, z))
	return z

def subtract(x, y):
	z = x - y
	print("{} - {} = {}" .format(x, y, z))
	return z

def multiply(x, y):
	z = x * y
	print("{} * {} = {}" .format(x, y, z))
	return z



x = input("Enter a letter: ")
print("You entered {}" .format(x))

if x == "a":
	add()
elif x == "b":
	d = add2(1, 2)
	if d > 100:
		print("This number is too high")
elif x == "s":
	d = subtract(20, -3)
elif x == "m":
	d = multiply(6, 5)
else:
	print("The {} command is not recognized." .format(x))