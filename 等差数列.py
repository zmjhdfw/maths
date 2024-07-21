x = int(input("请输入等差数列首项:"))
try:
    d = int(input("请输入等差数列公差:"))
except ValueError:
    print(f'抱歉无法获取公差')
    try:
        d = int(input("请重新输入："))
    except ValueError:
        for i in range(1):
            print(f'因为没有公差，所以无法计算，抱歉哈')
            break
n = int(input("请输入要求的项数:"))
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