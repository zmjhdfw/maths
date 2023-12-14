x = int(input("请输入运算的第一个数"))
y = int(input("请输入运算的第二个数"))
fr = int(input("请输入循环次数"))
for i in range(fr):
    if x > y:
        count = x/y
        print(f'结果:{count}')
    else:
        print(f'非法操作，不予执行。')