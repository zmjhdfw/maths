n = int(input("请输入运算的数字:"))
if n >= 2:
    for i in range(n):
        i*=(i+1)
else:
    i = 1
print(f'结果:{i}')