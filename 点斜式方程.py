x1=int(input(f'请输入第一个点的横坐标:'))
y1=int(input(f'请输入第一个点的纵坐标:'))
x2=int(input(f'请输入第二个点的横坐标:'))
y2=int(input(f'请输入第二个点的纵坐标:'))
k=(y2-y1)/(x2-x1)
b=y1-k*x1
if b>0 and isinstance(k,int):
    print(f'方程式为y={round(k)}x+{round(b)}')
elif b==0 and isinstance(k,int):
    print(f'方程式为y={round(k)}x')
elif b<0 and isinstance(k,int):
    print(f'方程式为y={round(k)}x{round(b)}')
elif b>0 and isinstance(k,float):
    print(f'方程式为y={k}x+{round(b)}')
elif b==0 and isinstance(k,float):
    print(f'方程式为y={k}x')
elif b<0 and isinstance(k,float):
    print(f'方程式为y={k}x{round(b)}')