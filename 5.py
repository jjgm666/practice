# 1.定义和调用函数

def max(num1, num2):  # 注意！！！这里仅仅是一个数字的输入，而不是比较的一个数！比如输入的是9和16比较，则实际上比较的是9和1，返回的是9
    if num1 > num2:
        result = num1
    else:
        result = num2
    return result


a = input("请输入第一个数字：")
b = input("请输入第二个数字：")
z = max(a, b)
print(z)
print(max(a, b))


def main():
    i = 5
    j = 2
    k = max(i, j)
    print(i, "和", j, "中更大的是：", k)


main()  # 调用main函数


# 2.带返回值和不带返回值的函数
def printSGrade_1(score):
    if score >= 90.0:
        print("A")
    elif score >= 80.0:
        print("B")
    elif score >= 70.0:
        print("C")
    elif score >= 60.0:
        print("D")
    else:
        print("Fail")


def main():
    score = eval(input("输入一个成绩："))
    print("成绩是：", end="")
    printSGrade_1(score)


main()


def printSGrade_2(score):
    if score >= 90.0:
        return 'A'
    elif score >= 80.0:
        return 'B'
    elif score >= 70.0:
        return 'C'
    elif score >= 60.0:
        return 'D'
    else:
        return 'Fail'


def main():
    score = eval(input("输入一个成绩："))
    print("成绩是：", printSGrade_2(score))


main()

# 变量的作用域
def function():
    x=4.5
    y=3.5
    print(x)
    print(y)

function()
'''
print(x)   # 报错
print(y)
'''

# 默认参数的设置和调用
def printArea(width =1,height=1):
    area = width*height
    print("Width:",width,"\tHeight:",height,"\tArea:",area)

printArea()
printArea(2,4.5)
printArea(height=5,width=3)
printArea(height=6.6)
printArea(width=2.2)

# 返回多个值
def multiSort(n1,n2):
    if n1 > n2:
        return n2,n1
    else:
        return n1,n2
n1,n2 = multiSort(5,3)
print("n1=",n1)
print("n2=",n2)
