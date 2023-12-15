x = int(input("请输入运算的数字:"))
n = int(input("请输入内指数幂"))
m = int(input("请输入外指数幂"))
for i in range(1):
    i = pow(x,(n/m))
print(f'结果:{i}')