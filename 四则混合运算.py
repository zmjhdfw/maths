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
print(f'1.加法  2.减法  3.乘法  4.除法  5.退出') #打印选项
for i in range(5): #控制输入次数
    if i == 4:
        print(f'抱 歉 已 达 输 入 上 限 , 请 明 日 再 来 .')
        break
    else:
        n = int(input("请输入选项:")) #输入选项
        if n == 1:
            a = addition() #定义选项1
        elif n == 2:
            s = subtraction() #定义选项2
        elif n == 3:
            m = multiplication() #定义选项3
        elif n == 4:
            d = division() #定义选项4
        elif n == 5:
            print(f'期 待 下 次 与 你 相 见 !') #定义选项5
            break
        else:
            print(f'非法操作,不予执行') #定义其他选项
            continue