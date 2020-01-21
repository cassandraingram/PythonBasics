# calculator.py
# Cassie Ingram (cji3)
# Jan 22, 2020

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

###### additional practice 

# prompt user to enter two numbers and the operation they 
# want to perform 
n1, n2, opp = input("Enter two integers and an operation, separated by a comma: ").split(", ")

# converet input numbers to integer type variables 
n1 = int(n1)
n2 = int(n2)

# perform action based on what was entered 
if opp == "add":
	solution = add(n1, n2)
	print("{} + {} = {}" .format(n1, n2, solution))
elif opp == "subtract":
	solution = subtract(n1, n2)
	print("{} - {} = {}" .format(n1, n2, solution))
elif opp == "multiply":
	solution = multiply(n1, n2)
	print("{} * {} = {}" .format(n1, n2, solution))
elif opp == "divide":
	solution = divide(n1, n2)
	print("{} / {} = {}" .format(n1, n2, solution))
else: 
	print("Not a valid operation.")


