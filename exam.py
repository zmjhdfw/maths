'''def test():
    a = int(input(f'please give a number:'))
    c = int(input(f'please give a number:'))
    if a < 0:
        for i in range(c):
            a += 1
        return a
    elif a >= 0:
        for i in range(c):
            a -= 1
        return a
    else: 
        print(f'非法输入')
print(f'answer is {test()}')
a = float(input(f'please give a number:'))
b = float(input(f'please give a number:'))
c = float
if a > b:
    c = a
else:
    c = b
print(f'max:{c}')'''
'''a = (1,2,3,4,5,5,5,'你好',[1,2,3,4,5,5],(1,2,3,4,5,5))
b = {2:'1',1:'2'}
c = False
print(type(c))
print(type(a))'''
'''n=eval(input('请输入:'))
s=0
f=1
for i in range(1,n+1):
    f*=i
    s+=f
print(f'{s}')'''
'''s = [1,2,3,4,5,6] #输出指定元素
print(s[0])
s1 = [1,2,3,4,5,6]
try: #异常报错控制
    n = int(input('请输入你要查找的元素序列:'))
    l = len(s1)
    if n>0 and n<l:
        print(s1[n-1]) #因为列表查找是从0开始，所以在输出时要n-1
    else:
        print('无法查找')
except ValueError:
    print('输入错误')'''
'''from string import Template as t
s2 = t('$who ')
s3= s2.substitute(who='零')
print(s2)
s6=[1,2,3]
s6.append(7)
print(s6[3])'''
'''n=int(input('please give me a number:'))
if 1<=n<=7:
    print(n)
    if n==1:
        a='Mo'
    elif n==2:
        a='Tu'
    elif n==3:
        a='We'
    elif n==4:
        a='Th'
    elif n==5:
        a='Fr'
    elif n==6:
        a='Sa'
    elif n==7:
        a='Su'
else:
    print(None)
print(a)'''
'''n=int(input('请输入尝试次数:'))
for i in range(n):
    try:
        s=int(input('请输入行数(1-9):'))
        if 1<=s<=9:
            break
        else:
            raise Exception
    except ValueError:
        continue
    except Exception as errror:
        continue'''
'''import time as te
def main()->None:
    sum=0
    while te.daylight<100:
        te.daylight+=1
        sum+=te.daylight
        te.sleep(te.daylight)
        print(f'这是第{te.daylight}次,用时{te.daylight}秒')
    while te.daylight>=100:
        print(f'这{te.daylight}次,共用时{sum}')
        break
main()'''
'''def main()->None:
    l1=[x**2 for x in range(10)]
    print(f'{l1}')
main()'''
'''import random
keySn=''
for i in range(5):
    s=''
    characters='BCEFGHJKMPQRTVXWY2346789'
    for j in range(5):
        s=s+random.choice(characters)
    if i==0:
        keySn=keySn+s
    else:
        keySn=keySn+'-'+s
print(f'密钥为{keySn}')'''
'''import random
a=b=int
x=random.randint(a=1,b=100)
print(f'{x}')'''
'''c=5
while c>0:
    print(f'剩余{c-1}次机会')
    c-=1'''
'''x = float(input("请输入等差数列首项:"))
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
n2 = int(input("请输入要求的前n项和的项数:"))
sum=0
for i in range(n2+1):
    if i%7!=0:
        sum+=x+(i-1)*d
    else:
        continue
print(f'结果{sum}')'''
'''while True:
    s=input()
    if s=='y' or s=='Y':
        break'''
'''def t_s(T):
    result=0
    for i in T:
        result+=i
    return result
print('(1,2,3,4)的元素和:',t_s((1,2,3,4)))
s=input(':')
s1=len(s)
print(f'位数:{s1}')
class test:
    def func():
        x=1
        y=2
        print(x)
        a=test.main()
        print(a)
    def main():
        x=1
        y=2
        print(y)
test.func()
x=1
print(x)
def main():
    y=2
    print(y)
main()
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# 参数范围
rho_air_values = np.linspace(1.0, 1.5, 10)  # 空气密度范围
r_values = np.linspace(0.0004, 0.0006, 10)  # 琴弦半径范围
rho_string_values = np.linspace(2500, 3000, 10)  # 琴弦密度范围

# 循环遍历参数
for idx, (rho_air, r, rho_string) in enumerate(np.ndindex(len(rho_air_values), len(r_values), len(rho_string_values))):
    rho_air = rho_air_values[idx // (len(r_values) * len(rho_string_values))]
    r = r_values[idx // len(rho_string_values) % len(r_values)]
    rho_string = rho_string_values[idx % len(rho_string_values)]
    
    # 参数设置
    L = 1.0  # 琴弦长度，单位：米
    E = 1.9e11  # 弹性模量，单位：帕斯卡
    beta = 0.1 * rho_air  # 阻尼系数，这里假设与空气密度成正比

    # 计算张力T和线密度μ
    A = np.pi * r**2  # 横截面积
    Delta_L = 0.01 * L  # 拉伸长度
    T = E * (Delta_L / L) * A  # 张力
    mu = rho_string * A  # 线密度

    # 计算波速
    c = np.sqrt(T / mu)

    # 时间和空间设置
    dx = 0.01  # 空间步长，减小以提高精度
    dt = dx / (2 * c)  # 时间步长，根据CFL条件设置
    x = np.arange(0, L, dx)  # 空间网格
    t = np.arange(0, 1, dt)  # 时间网格

    # 初始化琴弦位移和速度
    y = np.zeros((len(t), len(x)))
    v = np.zeros((len(t), len(x)))

    # 初始条件：在琴弦中间施加一个较小的脉冲
    y[0, (len(x) // 2 - 10):(len(x) // 2 + 10)] = 0.1

    # 模拟琴弦振动
    for i in range(1, len(t)):
        # 内部节点的速度更新
        v[i, 1:-1] = v[i-1, 1:-1] + (c * dt / dx) * (y[i-1, 2:] - 2*y[i-1, 1:-1] + y[i-1, :-2]) - (beta * dt / mu) * v[i-1, 1:-1]
        
        # 内部节点的位移更新
        y[i, 1:-1] = y[i-1, 1:-1] + dt * v[i, 1:-1]
        
        # 边界条件：假设琴弦两端固定
        y[i, 0] = 0  # 左端固定
        y[i, -1] = 0  # 右端固定
        v[i, 0] = 0  # 左端速度为0
        v[i, -1] = 0  # 右端速度为0

        # 检查是否出现NaN或Inf
        if np.any(np.isnan(y[i])) or np.any(np.isinf(y[i])):
            print(f"NaN 或 Inf 在第 {i} 步遇到，模拟停止")
            break

    # 绘制结果
    plt.figure(figsize=(12, 4))
    plt.plot(x, y[-1, :]),
label=f'ρ_air={rho_air}, r={r}

name=input('Please enter you name:')
print(f'\nHello,{name}')'''
num=1
if num>2:
    print('1')
else:
    print('2')