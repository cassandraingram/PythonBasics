# calculator.py

# add function adds two inputs
def add(x, y): 
	z = x + y
	return z

#subtract function subtracts two inputs
def subtract(x, y):
	z = x - y
	return z

# multiply function multiplies two inputs
def multiply(x, y):
	z = x * y
	return z

# divide function divides two inputs
def divide(x, y):
	z = x / y
	return z

# modulee calls each function using the numbers 47 and 7 and 
# then prints the results of each function
a = add(47, 7)
print("47 + 7 = {}" .format(a))
s = subtract(47, 7)
print("47 - 7 = {}" .format(s))
m = multiply(47, 7)
print("47 * 7 = {}" .format(m))
d = divide(47, 7)
print("47 / 7 = {}" .format(d))