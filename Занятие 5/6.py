a = input()
b = a.replace('f', ' ', 1)
s = b.find('f')
c = a.find('f')
if s >= 0:
    print(s)
elif c == -1:
    print(-2)
elif s == -1:
    print(-1)
