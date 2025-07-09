x = float(input("请输入等差数列首项:"))
try:
    d = float(input("请输入等差数列公差:"))
except ValueError:
    print(f'抱歉无法获取公差')
    try:
        d = float(input("请重新输入："))
    except ValueError:
        for i in range(1):
            print(f'因为没有公差，所以无法计算，抱歉哈')
            break
n1 = int(input("请输入要求的项数:"))
if x==0 and d==0:
    y1 = x
    print(f'这是首项为0,公差为0的常数数列,所以结果为{y1}')
elif x!=0 and d==0:
    y1 = x
    print(f'这是首项不为0,但公差为0的常数数列,所以结果为{y1}')
elif x==0 and d!=0:
    y1 = (n1-1)*d
    print(f'这是首项为0,但公差不为0的常数数列,所以结果为{y1}')
elif x!=0 and d!=0:
    y1 = x + (n1-1)*d
    print(f'结果为{y1}')
n2 = int(input("请输入要求的前n项和的项数:"))
if x==0 and d==0:
    y2 = x
    print(f'这是首项为0,公差为0的常数数列,所以前n项和为{y2}')
elif x!=0 and d==0:
    y2 = n2*x
    print(f'这是首项不为0,但公差为0的常数数列,所以前n项和为{y2}')
elif x==0 and d!=0:
    y2 = n2*((n2-1)*d/2)
    print(f'这是首项为0,但公差不为0的常数数列,所以前n项和为{y2}')
elif x!=0 and d!=0:
    y2 = n2*x+n2*((n2-1)*d/2)
    print(f'前n项和为{y2}')