import cmath

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a == 0:
	if b == 0:
		print("This is not a valid equation." if c != 0 else "Every value of x is a solution.")
	else:
		print(f"The solution is x = {-c / b:.2f}")
else:
	discriminant = b**2 - 4 * a * c
	root_1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
	root_2 = (-b - cmath.sqrt(discriminant)) / (2 * a)

	if discriminant >= 0:
		print(f"The roots are x1 = {root_1.real:.2f} and x2 = {root_2.real:.2f}")
	else:
		print(f"The complex roots are x1 = {root_1:.2f} and x2 = {root_2:.2f}")
