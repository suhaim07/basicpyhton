n = int(input("enter the table to print: "))
c = 0
for i in range(1,11):
    c = i * n
    print(f"{n} x {i} = {c}")