n = 58329
small_digit = n

while n > 0:
    digit = n % 10
    if digit < small_digit:
        small_digit = digit
    n //= 10
print(small_digit)