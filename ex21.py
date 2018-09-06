def add(a, b):
	print(f"ADDING {a} + {b}")
	return a+b

def subtract(a, b):
	print(f"SUBTRACTING {a} - {b}")
	return a -b

def multiply(a, b):
	print(f"MULTIPLYING {a} * {b}")
	return a * b

def divide (a, b):
	print(f"DIVIDING {a} / {b}")
	return a /b

def quad_equation(a, b, c):
	D= b**2 - 4 * a * c
	if D >= 0:
		x1 = (-b + D**0.5) / (2 * a)
		x2 = (-b - D**0.5) / (2 * a)
	else:
		x1 = False
		x2 = False
	return x1, x2
		
print("Let's do some match with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


#A puzzle for extra credit. type it in anyway
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

fa, sa = quad_equation(2, 5 , 3)
print(f"Roots of equation 2*x**2 + 5 * x + 3  = 0 is: x1 = {fa}, x2 = {sa}")
fa, sa = quad_equation(5, 5 , 3)
print(f"Roots of equation 5*x**2 + 5 * x + 3  = 0 is: x1 = {fa}, x2 = {sa}")

