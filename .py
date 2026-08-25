n = 58329
largest_digit = 0

while n > 0:
    digit = n % 10
    if digit > largest_digit:
        largest_digit = digit
    n //= 10

print("Largest digit:", largest_digit)