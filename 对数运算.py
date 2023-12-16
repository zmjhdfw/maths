import math
x = int(input("请输入运算的数字:"))
y = int(input("请输入底数:"))
if x > 0 and y > 0:
    for i in range(1):
        i = math.log(x,y)
    print(f'结果:{i}')
else:
    print(f'非法操作，不予执行')