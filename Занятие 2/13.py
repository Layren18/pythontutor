n = int(input())
m = int(input())
x = int(input())
y = int(input())
if n > m:
    l = n
    s = m
else:
    l = m
    s = n
a = [l-y,s-x,x,y]
print(min(a))
