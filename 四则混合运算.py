def addition(): #实现加法功能
    for i in range(1):
        count= x+y
    print(f'结果:{count}')
def subtraction(): #实现减法功能
    for i in range(1):
        count = x-y
    print(f'结果:{count}')
def multiplication(): #实现乘法功能
    for i in range(1):
        count = x*y
    print(f'结果:{count}')
def division(): #实现除法功能
    for i in range(1):
        if x >= y:
            count = x/y
            print(f'结果:{count}')
        else:
            print(f'非法操作，不予执行。')
#主函数
for i in range(5): #打印欢迎界面
    if i == 0 or i == 4:
        print(f'***************************')
    elif i == 1 or i == 3:
        print(f'                           ')
    else:
        print(f'欢 迎 使 用 四 则 混 合 运 算')
        continue
x = int(input("请输入运算的数字:")) #输入x变量的值
y = int(input("请输入运算的数字:")) #输入y变量的值
n = input("请输入选项:")
a = addition() #定义选项a
s = subtraction() #定义选项s
m = multiplication() #定义选项m
d = division() #定义选项d