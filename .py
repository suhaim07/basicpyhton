number = input("Enter a number: ")
chosen_digit = input("Enter the digit to count (0-9): ")

if len(chosen_digit) != 1 or not chosen_digit.isdigit():
    print("Please enter exactly one digit.")
else:
    print(f"The digit {chosen_digit} appears {number.count(chosen_digit)} time(s).")