#本代码实际应用于等比数列首项，公比都已知的情况下
try: #try-except语句控制异常报错
    x = int(input("请输入等比数列首项:")) #要求用户输入首项
    q = int(input("请输入等比数列公比:")) #要求用户输入公比
    n = int(input("请输入要求的项数:")) #要求用户输入项数
    if n!=0: #如果n不为0的情况
        if x==0: #定义第一种情况
            print(f'非法操作')
        elif x!=0 and q==0: #定义第二种情况
            y = x
            print(f'这是首项不为0,但公差为0的常数数列,所以结果为{y}')
        elif x==0 and q!=0: #定义第三种情况
            y = (n-1)*q
            print(f'这是首项为0,但公差不为0的常数数列,所以结果为{y}')
        elif x!=0 and q!=0: #定义第四种情况
            y = x + (n-1)*q
            print(f'结果为{y}')
    else: #如果n为0的情况
        print(f'项数为0无法计算,抱歉哈')
except ValueError: #代码报错输出的情况
    print(f'公比为空值无法计算,抱歉哈')