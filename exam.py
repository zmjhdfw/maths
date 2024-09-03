'''def test():
    a = int(input(f'please give a number:'))
    c = int(input(f'please give a number:'))
    if a < 0:
        for i in range(c):
            a += 1
        return a
    elif a >= 0:
        for i in range(c):
            a -= 1
        return a
    else: 
        print(f'非法输入')
print(f'answer is {test()}')'''
a = float(input(f'please give a number:'))
b = float(input(f'please give a number:'))
c = float
if a > b:
    c = a
else:
    c = b
print(f'max:{c}')