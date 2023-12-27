#本代码实际应用于等差数列首项，公差有一项未知的情况下
try: #try-except语句控制异常报错
    for i in range(1):
        print(f'1.缺失首项 2.缺失公差 3.退出')
        n = int(input("请输入选项:"))
        if n  == 1:
            d = int(input("请输入公差:"))
            n = int(input("请给出已知项:"))
            y = int(input("请给出对应的值:"))
            for i in range(1):
                x = y - (n-1)*d
            print(f'首项为{x}')
            print(f'是否继续')
            m = input("请选择:")
            if m == '是' or m == 'yes':
                n = int(input("请输入要求的项"))
                for i in range(1):
                    y = x + (n-1)*d
                print(f'结果为{y}')
            elif m == '否' or m == 'no':
                break
            else:
                break
        elif n == 2:
            x = int(input("请输入首项:"))
            n = int(input("请给出已知项:"))
            y = int(input("请给出对应的值:"))
            for i in range(1):
                d = (y-x) / (n-1)
            print(f'公差为{d}')
            print(f'是否继续')
            m = input("请选择:")
            if m == '是' or m == 'yes':
                n = int(input("请输入要求的项:"))
                for i in range(1):
                    y = x + (n-1)*d
                print(f'结果为{y}')
            elif m == '否' or m == 'no':
                break
            else:
                break
        elif n == 3:
            print(f'期 待 下 次 与 你 相 见')
        else:
            print(f'非 法 操 作 , 不 予 执 行')
except ValueError:
    print(f'空着给我填，想得美，哼！')