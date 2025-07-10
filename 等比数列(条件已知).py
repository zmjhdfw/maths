#本代码实际应用于等比数列首项，公比都已知的情况下
try: #try-except语句控制异常报错
    x = int(input("请输入等比数列首项:")) #要求用户输入首项
    q = int(input("请输入等比数列公比:")) #要求用户输入公比
    n = int(input("请输入要求的项数:")) #要求用户输入项数
    if x<0 or q<0 or n<0:
        print(f'非法操作')
    else:
        if n!=0: #如果n不为0的情况
            if x==0 or q==0: #定义第一种情况
                print(f'非法操作')
            elif x!=1 and q!=1: #定义第二种情况
                y=x*pow(q,n-1)
                print(f'这是首项为{x},公比为{q}的等比数列，结果是{y}')
            elif x==1: #定义第三种情况
                y=pow(q,n-1)
                print(f'这是首项为{x},公比为{q}的常数数列，结果是{y}')
            elif q==1: #定义第四种情况
                y=x
                print(f'这是首项为{x},公比为{q}的常数数列，结果是{y}')
        else: #如果n为0的情况
            print(f'项数为0无法计算')
except ValueError: #代码报错输出的情况
    print(f'违法输入')