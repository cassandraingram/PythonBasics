# basics
x = input("Enter a letter: ")

# basic print statements
print("You entered {}" .format(x))
#print("This is a linee of code.")
#print(x)
#print(16.4)

# some math
if x == "a":
	a = 1
	b = 2
	c = a + b
	print("{} + {} = {}" .format(a, b, c))
elif x == "s":
	a = 20 
	b = -3
	c = a - b
	print("{} - {} = {}" .format(a, b, c))
elif x == "m":
	a = 6
	b = 5
	c = a * b
	print("{} * {} = {}" .format(a, b, c))
else:
	print("The {} command is not recognized." .format(x))

print("Done")
