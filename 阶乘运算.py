m = int(input("请输入要运算的数字:"))
n = int(input("请输入阶乘数:"))
for i in range(n):
    m*=(i+1)
print(f'结果:{m}')