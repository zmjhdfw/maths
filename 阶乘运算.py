n = int(input("请输入运算的数字:"));m = 1
if n > 1:
    for i in range(n):
        m*=(i+1)
    print(f'结果:{m}')
else:
    print(f'结果:{m}')