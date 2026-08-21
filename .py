a = [1,2,3,4]
n = 0
b = a[n]
c= a[0]

for i in a:
    if i > b:
        b = i
print(i)

for j in a:
    if j < c:
        c = j

print(c)