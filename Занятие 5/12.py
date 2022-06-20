a = input()
b = ''
for i in range(len(a)):
    if i % 3 != 0:
        b = b + a[i]
print(b)
