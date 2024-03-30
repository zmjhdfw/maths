#本代码实际应用于等差数列首项，公差都未知的情况下
import math
try: #try-except语句控制异常报错
    def Arithmetic_sequence_unknown(): #自定义函数
        for i in range(1): #进行一次for循环
            print(f'1.求解公差 2.求解首项 3.退出') #打印选项
            n1 = int(input(f'请输入选项:')) #用户输入选项
            if n1  == 1: #选项1的情况
                print(f'1.已知x1,x2为等差数列的两项且是一元二次函数的两个实数解\n2.已知前n-1项的和,前n项的和与前n+1的和\n3.退出')
                n2 = int(input(f'请输入选项:'))
                if  n2 == 1:
                    a = int(input(f'请输入a的值:'))
                    b = int(input(f'请输入b的值:'))
                    c = int(input(f'请输入c的值:'))
                    q = b**2-2(a*c)
                    if q == 0:
                        x1,x2 = -b/(2*a)
                        d = 0
                        print(f'公差为{d}')
                    if q > 0:
                        x1 = -b+math.sqrt(q)/(2*a)
                        x2 = -b-math.sqrt(q)/(2*a)
                        print(f'1.公差为负\n2.公差为正')
                        c1 = print(f'请输入选项:')
                        if c1 == 1:
                            d = x2 - x1
                            print(f'公差为{d}')
                        elif c1 == 2:
                            d = x1 - x2
                            print(f'公差为{d}')
                        else:
                            print(f'不存在，终止程序')
                            break
                    if q < 0:
                        print(f'不存在,终止程序')
                        break
                elif n2 == 2:
                    s1 =int(input(f'请输入前n项的和:'))
                    s2 =int(input(f'请输入前n-1项的和:'))
                    s3 =int(input(f'请输入前n+1项的和:'))
                    q1 = s1-s2
                    q2 = s3-s1
                    d = q2-q1
                    print(f'a(n)项的值为{q1},a(n+1)项的值为{q2},公差为{d}')
                elif n2 == 3:
                    print(f'感谢使用，拜拜')
                    break
                else:
                    print(f'不存在，终止程序')
                    break
            elif n1 == 2:
                print(f'')
                d = int(input("请输入公差:")) #用户输入公差
                n = int(input("请给出已知项:")) #用户输入已知项
                y = int(input("请给出对应的值:")) #用户输入对应的值
                for i in range(1): #进行一次for循环
                    x = y - (n-1)*d #求出首项
                print(f'首项为{x}') #打印出首项
                print(f'是否继续') #给出选择
                m = input("请选择:") #用户输入选择
                if m == '是' or m == 'yes': #判断用户的选择，为'是'或'yes'
                    n = int(input("请输入要求的项")) #用户输入要求的项
                    for i in range(1): #进行一次循环
                        y = x + (n-1)*d #求出对应的值
                    print(f'结果为{y}') #打印出对应的值
                elif m == '否' or m == 'no': #判断用户的选择，为'否'或'no'
                    break #结束程序
                else: #其他情况
                    break #结束程序
            elif n == 2: #选项2的情况
                x = int(input("请输入首项:")) #用户输入首项
                n = int(input("请给出已知项:")) #用户输入已知项
                y = int(input("请给出对应的值:")) #用户输入对应的值
                for i in range(1): #进行一次for循环
                    d = (y-x) / (n-1) #求出公差
                print(f'公差为{d}') #打印公差
                print(f'是否继续') #给出选择
                m = input("请选择:") #用户输入选择
                if m == '是' or m == 'yes': #判断用户的选择，为'是'或'yes'
                    n = int(input("请输入要求的项:")) #用户输入要求的项
                    for i in range(1): #进行一次循环
                        y = x + (n-1)*d #求出对应的值
                    print(f'结果为{y}') #打印出对应的值
                elif m == '否' or m == 'no': #判断用户的选择，为'否'或'no'
                    break #结束程序
                else: #其他情况
                    break #结束程序
            elif n == 3: #选项3的情况
                print(f'期 待 下 次 与 你 相 见') #打印结束语
            else: #其他情况
                print(f'非 法 操 作 , 不 予 执 行') #打印警告语
except ValueError: #代码报错输出的情况
    print(f'空着给我填，想得美，哼！') #打印一段话，可自定义
x = x1
p = x + (n-1)*d
print(f'等差数列首项:{x},公差:{d},通项公式:{p}')