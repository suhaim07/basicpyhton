number = input("Enter a number: ")

if not number.lstrip("-").isdigit():
    print("Please enter a valid number.")
else:
    digits = sorted(set(number) - {"-"}, reverse=True)

    if len(digits) < 2:
        print("The number does not have a second-largest digit.")
    else:
        print(f"The second-largest digit is {digits[1]}.")