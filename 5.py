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
