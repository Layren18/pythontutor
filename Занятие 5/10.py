a = input()
while a.find('@') >= 0:
    a = a[:a.find('@')] + a[a.find('@') + 1:]
print(a)
