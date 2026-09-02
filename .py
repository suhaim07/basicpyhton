term_count = int(input("How many Fibonacci terms do you want? "))

if term_count <= 0:
	print("Please enter a positive number of terms.")
else:
	sequence = []
	first, second = 0, 1

	for _ in range(term_count):
		sequence.append(first)
		first, second = second, first + second

	print("Fibonacci sequence:", sequence)
