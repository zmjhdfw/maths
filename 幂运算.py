number = int(input("请输入要打印的数字:"))
n = int(input("请输入初始幂指数:"))
m = int(input("请输入终止幂指数:"))
for i in range (n,m+1):
    print (pow(number,i))
    i = i+1