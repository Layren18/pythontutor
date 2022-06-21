n = int(input())
a = 1
while 2**a <= n:
    a = a + 1
print(a-1, 2**(a-1))
