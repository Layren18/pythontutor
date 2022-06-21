n = -1
b = 0
a = int(input())
len = 0
while a != 0:
    if a > b:
        b = a
        n = len
    a = int(input())
    len = len + 1
print(n)
