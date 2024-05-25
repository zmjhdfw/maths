#本代码实际应用于等差数列首项，公差都未知的情况下
import math  #导入数学库
try: #try-except语句控制异常报错
    def Arithmetic_sequence_unknown(): #自定义函数
        for i in range(4): #进行4次循环
            if i != 3: # 判断是否为第四次循环
                print(f'1.求解公差 2.求解首项 3.退出') #打印选项
                n1 = int(input(f'请输入选项:')) #用户输入选项
                if n1  == 1: #选项1的情况
                    print(f'1.已知x1,x2为等差数列的两项且是一元二次函数的两个实数解\n2.已知前n-1项的和,前n项的和与前n+1的和\n3.退出') #打印选项
                    n2 = int(input(f'请输入选项:')) #用户输入选项
                    if  n2 == 1: #选项1的情况
                        a = int(input(f'请输入a的值:'))
                        b = int(input(f'请输入b的值:'))
                        c = int(input(f'请输入c的值:'))
                        q = b**2-2*(a*c)
                        if q == 0:
                            x1 = x2 = -b/(2*a)
                            d = 0
                            print(f'公差为{d}')
                        elif q > 0:
                            x1 = -b+math.sqrt(q)/(2*a)
                            x2 = -b-math.sqrt(q)/(2*a)
                            print(f'1.公差为负\n2.公差为正')
                            c1 = int(input(f'请输入选项:'))
                            if c1 == 1: #选项1的情况
                                d = x2 - x1
                                print(f'公差为{round(d)}')
                            elif c1 == 2: #选项2的情况
                                d = x1 - x2
                                print(f'公差为{round(d)}')
                            else:
                                print(f'不存在，终止程序')
                                break
                        elif q < 0:
                            print(f'不存在,终止程序')
                            break
                    elif n2 == 2: #选项2的情况
                        s1 =int(input(f'请输入前n项的和:'))
                        s2 =int(input(f'请输入前n-1项的和:'))
                        s3 =int(input(f'请输入前n+1项的和:'))
                        q1 = s1-s2
                        q2 = s3-s1
                        d = q2-q1
                        print(f'a(n)项的值为{q1},a(n+1)项的值为{q2},公差为{d}')
                    elif n2 == 3: #选项3的情况
                        print(f'感谢使用，拜拜')
                        break
                    else:
                        print(f'不存在，终止程序')
                        break
                elif n1 == 2: #选项2的情况
                    print(f'1.由上题已求得公差,又已知其中一项的项数\n2.由上题已求得公差,又已知前n项和的项数\n3.退出')
                    n2 =  int(input(f'请输入选项:'))
                    if n2 == 1: #选项1的情况
                        if q == 0:
                            x = x1 = x2
                            p = f'{round(x)} + (n-1)*{round(d)}'
                            print(f'等差数列首项:{round(x)},公差:{round(d)},通项公式:{p}')
                        elif q > 0:
                            n3 = int(input(f'x1的项:'))
                            if d > 0:
                                x = x1 - ((n3 - 1)*d)
                                p = f'{round(x)} + (n-1)*{round(d)}'
                                print(f'等差数列首项:{round(x)},公差:{round(d)},通项公式:{p}')
                            elif d < 0:
                                x = x1 - ((n3 - 1)*d)
                                p = f'{round(x)} + (n-1)*{round(d)}'
                                print(f'等差数列首项:{round(x)},公差:{round(d)},通项公式:{p}')
                            else:
                                print(f'不存在，终止程序')
                        else:
                            print(f'不存在，终止程序')
                    elif n2 == 2: #选项2的情况
                        n4 = int(input(f'请输入前n项的项数:'))
                        x = (2*s1)/n4-q1
                        p = f'{round(x)} + (n-1)*{round(d)}'
                        print(f'等差数列首项:{round(x)},公差:{round(d)},通项公式:{p}')
                    elif n2 == 3: #选项3的情况
                        print(f'感谢使用，拜拜')
                        break
                    else:
                        print(f'不存在，终止程序')
                        break
                elif n1 == 3: #选项3的情况
                    print(f'感谢使用，拜拜')
                    break
                else:
                    print(f'不存在，终止程序')
                    break
            elif i == 3: #第四次循环的情况
                print(f'感谢使用，拜拜')
                break
            else:
                print(f'不存在，终止程序')
                break
    asu = Arithmetic_sequence_unknown() #主函数
except ValueError: #代码报错输出的情况
    print(f'空着给我填，想得美，哼！') #打印一段话，可自定义