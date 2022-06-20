a = input()
if a.find('f') == -1:
    print()
elif a.find('f') == a.rfind('f'):
    print(a.find('f'))
else:
    print(a.find('f'), a.rfind('f'))
