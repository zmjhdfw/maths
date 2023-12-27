#本代码实际应用于等差数列首项，公差有一项未知的情况下
try: #try-except语句控制异常报错
    for i in range(1): #进行一次for循环
        print(f'1.缺失首项 2.缺失公差 3.退出') #打印选项
        n = int(input("请输入选项:")) #用户输入选项
        if n  == 1: #选项1的情况
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