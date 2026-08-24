n = int(input("factorial of: "))
fact = 1

if n == 1:
    print("0")
elif n < 0:
    print("-ve does not exist")
for i in range(1,n+1):
    fact *= i
print(fact)





