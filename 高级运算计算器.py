class logarithm(): #定义对数运算类
    def addition(): #定义对数加法功能（可根据需要自主修改） 
        for i in range(1):
            n = 1
            n = math.log(x1,y1)
        for i in range(1):
            m = 1
            m = math.log(x2,y2)
        for i in range(1):
            i = n + m
        print(f'结果:{i}')
    def subtraction(): #定义对数减法功能（可根据需要自主修改）
        for i in range(1):
            n = 1
            n = math.log(x1,y1)
        for i in range(1):
            m = 1
            m = math.log(x2,y2)
        for i in range(1):
            i = n - m
        print(f'结果:{i}')
    def multiplication(): #定义对数乘法功能（可根据需要自主修改）
        for i in range(1):
            n = 1
            n = math.log(x1,y1)
        for i in range(1):
            m = 1
            m = math.log(x2,y2)
        for i in range(1):
            i = n * m
        print(f'结果:{i}')
    def division(): #定义对数除法功能（可根据需要自主修改）
        for i in range(1):
            n = 1
            n = math.log(x1,y1)
        for i in range(1):
            m = 1
            m = math.log(x2,y2)
        if n >= m:
            for i in range(1):
                i = n / m
            print(f'结果:{i}')
        else:
            print(f'非法操作，不予执行')
class power(): #定义幂运算类
    def addition(): #定义幂加法功能（可根据需要自主修改） 
        for i in range(1):
            n = 1
            n = pow(x1,y1)
        for i in range(1):
            m = 1
            m = pow(x2,y2)
        for i in range(1):
            i = n + m
        print(f'结果:{i}')
    def subtraction(): #定义幂减法功能（可根据需要自主修改）
        for i in range(1):
            n = 1
            n = pow(x1,y1)
        for i in range(1):
            m = 1
            m = pow(x2,y2)
        for i in range(1):
            i = n - m
        print(f'结果:{i}')
    def multiplication(): #定义幂乘法功能（可根据需要自主修改）
        for i in range(1):
            n = 1
            n = pow(x1,y1)
        for i in range(1):
            m = 1
            m = pow(x2,y2)
        for i in range(1):
            i = n * m
        print(f'结果:{i}')
    def division(): #定义幂除法功能（可根据需要自主修改）
        for i in range(1):
            n = 1
            n = pow(x1,y1)
        for i in range(1):
            m = 1
            m = pow(x2,y2)
        if n >= m:
            for i in range(1):
                i = n/m
            print(f'结果:{i}')
        else:
            print(f'非法操作，不予执行')
class root(): #定义开方运算类
    def addition(): #定义开方加法功能（可根据需要自主修改） 
        for i in range(1):
            n = 1
            n = pow(x1,(n1/m1))
        for i in range(1):
            m = 1
            m = pow(x2,(n2/m2))
        for i in range(1):
            i = n + m
        print(f'结果:{i}')
    def subtraction(): #定义开方减法功能（可根据需要自主修改）
        for i in range(1):
            n = 1
            n = pow(x1,(n1/m1))
        for i in range(1):
            m = 1
            m = pow(x2,(n2/m2))
        for i in range(1):
            i = n - m
        print(f'结果:{i}')
    def multiplication(): #定义开方乘法功能（可根据需要自主修改）
        for i in range(1):
            n = 1
            n = pow(x1,(n1/m1))
        for i in range(1):
            m = 1
            m = pow(x2,(n2/m2))
        for i in range(1):
            i = n * m
        print(f'结果:{i}')
    def division(): #定义开方除法功能（可根据需要自主修改）
        for i in range(1):
            n = 1
            n = pow(x1,(n1/m1))
        for i in range(1):
            m = 1
            m = pow(x2,(n2/m2))
        if n >= m:
            for i in range(1):
                i = n / m
            print(f'结果:{i}')
        else:
            print(f'非法操作，不予执行')
class factorial(): #定义阶乘运算类
    def addition(x1,x2): #定义阶乘加法功能（可根据需要自主修改） 
        if x1 > 1:
            n = 1
            for i in range(x1):
                n*=(i+1)
        else:
            n = 1
        if x2 > 1:
            m = 1
            for i in range(x2):
                m*=(i+1)
        else:
            m = 1
        for i in range(1):
            i = n + m
        print(f'结果:{i}')
    def subtraction(x1,x2): #定义阶乘减法功能（可根据需要自主修改）
        if x1 > 1:
            n = 1
            for i in range(x1):
                n*=(i+1)
        else:
            n = 1
        if x2 > 1:
            m = 1
            for i in range(x2):
                m*=(i+1)
        else:
            m = 1
        for i in range(1):
            i = n - m
        print(f'结果:{i}')
    def multiplication(x1,x2): #定义阶乘乘法功能（可根据需要自主修改）
        if x1 > 1:
            n = 1
            for i in range(x1):
                n*=(i+1)
        else:
            n = 1
        if x2 > 1:
            m = 1
            for i in range(x2):
                m*=(i+1)
        else:
            m = 1
        for i in range(1):
            i = n * m
        print(f'结果:{i}')
    def division(x1,x2): #定义阶乘除法功能（可根据需要自主修改）
        if x1 > 1:
            n = 1
            for i in range(x1):
                n*=(i+1)
        else:
            n = 1
        if x2 > 1:
            m = 1
            for i in range(x2):
                m*=(i+1)
        else:
            m = 1
        if n >= m:
            for i in range(1):
                i = n - m
            print(f'结果:{i}')
        else:
            print(f'非法操作，不予执行')
class absolute(): #定义绝对值运算类
    def addition(): #定义绝对值加法功能（可根据需要自主修改）
        for i in range(1):
            n = 1
            n = abs(x1)
        for i in range(1):
            m = 1
            m = abs(x2)
        for i in range(1):
            i = n + m
        print(f'结果:{i}')
    def subtraction(): #定义绝对值减法功能（可根据需要自主修改）
        for i in range(1):
            n = 1
            n = abs(x1)
        for i in range(1):
            m = 1
            m = abs(x2)
        for i in range(1):
            i = n - m
        print(f'结果:{i}')
    def multiplication(): #定义绝对值乘法功能（可根据需要自主修改）
        for i in range(1):
            n = 1
            n = abs(x1)
        for i in range(1):
            m = 1
            m = abs(x2)
        for i in range(1):
            i = n * m
        print(f'结果:{i}')
    def division(): #定义绝对值除法功能（可根据需要自主修改）
        for i in range(1):
            n = 1
            n = abs(x1)
        for i in range(1):
            m = 1
            m = abs(x2)
        if n >= m:
            for i in range(1):
                i = n / m    
            print(f'结果:{i}')
        else:
            print(f'非法操作，不予执行')
#主函数
import math #导入数学库
for i in range(5): #打印欢迎界面
    if i == 0 or i == 4:
        print(f'********************************')
    elif i == 1 or i == 3:
        print(f'                                ')
    else:
        print(f'欢 迎 使 用 高 级 运 算 计 算 器')
        continue
for i in range(7): #控制输入次数
    if i == 6:
        print(f'抱歉已达输入上限,请明日再来.')
        break
    else:
        print(f'1.对数运算 2.幂运算 3.开方运算 4.阶乘运算 5.绝对值运算 6.退出') #打印运算类
        n = int(input("请输入运算功能:")) #输入运算类
    if n == 1:
        x1 = int(input("请输入运算的第一组数字:")) 
        y1 = int(input("请输入运算的第一组数字的底数:"))
        x2 = int(input("请输入运算的第二组数字:"))
        y2 = int(input("请输入运算的第二组数字的底数:"))
        for i in range(6): #控制输入次数
            if i == 5:
                print(f'抱 歉 已 达 输 入 上 限 , 请 明 日 再 来 .')
                break
            else:
                print(f'1.对数加法  2.对数减法  3.对数乘法  4.对数除法  5.返回主菜单') #打印选项
                n = int(input("请输入选项:")) #输入选项
            if n == 1:
                la = logarithm.addition() #定义选项1
            elif n == 2:
                ls = logarithm.subtraction() #定义选项2
            elif n == 3:
                lm = logarithm.multiplication() #定义选项3
            elif n == 4:
                ld = logarithm.division() #定义选项4
            elif n == 5:
                print(f'期 待 下 次 与 你 相 见 !') #定义选项5
                break
            else:
                print(f'非法操作,不予执行') #定义其他选项
                continue
    elif n == 2:
        x1 = int(input("请输入运算的第一组数字:"))
        y1 = int(input("请输入运算的第一组数字的幂指数:"))
        x2 = int(input("请输入运算的第二组数字:"))
        y2 = int(input("请输入运算的第二组数字的幂指数:"))
        for i in range(6): #控制输入次数
            if i == 5:
                print(f'抱 歉 已 达 输 入 上 限 , 请 明 日 再 来 .')
                break
            else:
                print(f'1.幂运算加法 2.幂运算减法 3.幂运算乘法 4.幂运算除法 5.返回主菜单')
                n = int(input("请输入选项:")) #输入选项
            if n == 1:
                pa = power.addition() #定义选项1
            elif n == 2:
                ps = power.subtraction() #定义选项2
            elif n == 3:
                pm = power.multiplication() #定义选项3
            elif n == 4:
                pd = power.division() #定义选项4
            elif n == 5:
                print(f'期 待 下 次 与 你 相 见 !') #定义选项5
                break
            else:
                print(f'非法操作,不予执行') #定义其他选项
                continue
    elif n == 3:
        x1 = int(input("请输入运算的第一组数字:"))
        n1 = int(input("请输入运算的第一组数字的内指数幂:"))
        m1 = int(input("请输入运算的第一组数字的外指数幂:"))
        x2 = int(input("请输入运算的第二组数字:"))
        n2 = int(input("请输入运算的第二组数字的内指数幂:"))
        m2 = int(input("请输入运算的第二组数字的外指数幂:"))
        for i in range(6): #控制输入次数
            if i == 5:
                print(f'抱 歉 已 达 输 入 上 限 , 请 明 日 再 来 .')
                break
            else:
                print(f'1.开方运算加法 2.开方运算减法 3.开方运算乘法 4.开方运算除法 5.返回主菜单')
                n = int(input("请输入选项:")) #输入选项
            if n == 1:
                ra = root.addition() #定义选项1
            elif n == 2:
                rs = root.subtraction() #定义选项2
            elif n == 3:
                rm = root.multiplication() #定义选项3
            elif n == 4:
                rd = root.division() #定义选项4
            elif n == 5:
                print(f'期 待 下 次 与 你 相 见 !') #定义选项5
                break
            else:
                print(f'非法操作,不予执行') #定义其他选项
                continue
    elif n == 4:
        x1 = int(input("请输入运算的第一组数字:"))
        x2 = int(input("请输入运算的第二组数字:"))
        for i in range(6): #控制输入次数
            if i == 5:
                print(f'抱 歉 已 达 输 入 上 限 , 请 明 日 再 来 .')
                break
            else:
                print(f'1.阶乘运算加法 2.阶乘运算减法 3.阶乘运算乘法 4.阶乘运算除法 5.返回主菜单')
                n = int(input("请输入选项:")) #输入选项
            if n == 1:
                fa = factorial.addition(x1,x2) #定义选项1
            elif n == 2:
                fs = factorial.subtraction(x1,x2) #定义选项2
            elif n == 3:
                fm = factorial.multiplication(x1,x2) #定义选项3
            elif n == 4:
                fd = factorial.division(x1,x2) #定义选项4
            elif n == 5:
                print(f'期 待 下 次 与 你 相 见 !') #定义选项5
                break
            else:
                print(f'非法操作,不予执行') #定义其他选项
                continue
    elif n == 5:
        x1 = int(input("请输入运算的第一组数字:"))
        x2 = int(input("请输入运算的第二组数字:"))
        for i in range(6): #控制输入次数
            if i == 5:
                print(f'抱 歉 已 达 输 入 上 限 , 请 明 日 再 来 .')
                break
            else:
                print(f'1.绝对值运算加法 2.绝对值运算减法 3.绝对值运算乘法 4.绝对值运算除法 5.返回主菜单')
                n = int(input("请输入选项:")) #输入选项
            if n == 1:
                aba = absolute.addition() #定义选项1
            elif n == 2:
                abS = absolute.subtraction() #定义选项2
            elif n == 3:
                abm = absolute.multiplication() #定义选项3
            elif n == 4:
                abd = absolute.division() #定义选项4
            elif n == 5:
                print(f'期 待 下 次 与 你 相 见 !') #定义选项5
                break
            else:
                print(f'非法操作,不予执行') #定义其他选项
                continue
    elif n == 6:
        print(f'期 待 下 次 与 你 相 见 !')
        break
    else:
        print(f'非法操作，不予执行')
        continue