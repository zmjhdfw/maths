number1 = int(input("请输入运算的第一个数:"))
number2 = int(input("请输入运算的第二个数:"))
fr = int(input("请输入循环次数:"))
count = 0
for i in range(fr):
    count= number1+number2
    print(count)
    number1 = count
    number2 = count