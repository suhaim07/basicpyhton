number = int(input("Enter a number: "))
divisor = int(input("Enter another number: "))

if divisor == 0:
	print("A number cannot be divided by zero.")
elif number % divisor == 0:
	print(f"{number} is divisible by {divisor}.")
else:
	print(f"{number} is not divisible by {divisor}.")
