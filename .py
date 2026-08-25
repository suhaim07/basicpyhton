n = 1221
original = n
reversed_number = 0

while n > 0:
    digit = n % 10
    reversed_number = reversed_number * 10 + digit
    n //= 10

if original == reversed_number:
    print("Palindrome")
else:
    print("Not a palindrome")