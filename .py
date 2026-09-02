number = int(input("Enter a positive number: "))

if number <= 0:
	print("Please enter a positive number.")
else:
	natural_numbers = list(range(1, number + 1))
	print("Natural numbers:", natural_numbers)
