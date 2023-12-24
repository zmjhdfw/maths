#本代码实际应用于等差数列首项，公差都已知的情况下
try:
    x = int(input("请输入等差数列首项:")) #要求用户输入首项
    d = int(input("请输入等差数列公差:")) #要求用户输入公差
    n = int(input("请输入要求的项数:")) #要求用户输入项数
    if n !=0:
        if x==0 and d==0:
            y = x
            print(f'这是首项为0,公差为0的常数数列,所以结果为{y}')
        elif x!=0 and d==0:
            y = x
            print(f'这是首项不为0,但公差为0的常数数列,所以结果为{y}')
        elif x==0 and d!=0:
            y = (n-1)*d
            print(f'这是首项为0,但公差不为0的常数数列,所以结果为{y}')
        elif x!=0 and d!=0:
            y = x + (n-1)*d
            print(f'结果为{y}')
    else:
        print(f'项数为0无法计算,抱歉哈')
except ValueError:
    print(f'公差为空值无法计算,抱歉哈')