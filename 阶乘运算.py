n = int(input("请输入运算的数:"))
if n >= 2:
    for i in range(n):
        i*=(i+1)
    print(f'结果:{i}')
else:
    print(f'结果:1')