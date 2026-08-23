
a = [1,2,2,3,4,4,4]
b = int(input("enter the number: "))
c = False

for i in a:
    if i == b:
        c = True
        break

if c:
    print(f"{b} exists")

else:
    print(f"{b} does not exists")