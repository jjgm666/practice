# 选择

# 布尔表达式、数值表达式
radius = 1
print(radius > 0)
print(radius < 0)
print(int(radius > 0))
print(int(radius < 0))

# 产生随机数  random()函数,需要引入random包,用法是：random.randint(a , b)  返回的是从a到b的随机整数；
#                                        也可以用random.randrange(a , b)  返回的是从a到b-1的随机整数；
#                                        还可以用random.random()     返回的是从0.0到1.0的随机浮点数；
import random

number1 = random.randint(0, 20)
number2 = random.randint(0, 20)
answer = eval(input("What is " + str(number1) + "+" + str(number2) + "?"))
print(number1, "+", number2, "=", answer, "is", number1 + number2 == answer)

# if语句
score = eval(input("输入成绩："))
if score >= 90:
    grade = 'A'
else:
    if score >= 80:
        grade = "B"
    else:
        if score >= 70:
            grade = 'C'
        else:
            if score >= 60:
                grade = 'D'
            else:
                grade = 'E'
print("Grade is :", grade)

score1 = eval(input("输入成绩1："))
if score1 >= 90:
    grade = 'A'
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print("Grade is :", grade)

# 逻辑运算符 not 逻辑否、and 逻辑和、or 逻辑或
number = eval(input("输入一个整数:"))

if number % 2 == 0 and number % 3 == 0:
    print("这个数能被2和3整除！")
elif number % 2 == 0 or number % 3 == 0:
    print("这个数能被2或3整除！")
elif (number % 2 == 0 or number % 3 == 0) and not (number % 2 == 0 and number % 3 == 0):
    print("这个数能被2或3整除,但不能被2或3整除！")

# 条件表达式  条件1 if 布尔表达式 else 条件2
x = eval(input("请输入x值："))
y = 1 if x > 0 else -1
print(y)
"""
等同于：
if x > 0:
    y = 1
else
    y = -1
"""
# 运算符优先级 和 结合方向
"""
高       +   -   （一元    加减运算符）
|       **  
|       not
|       *   /   //  %
|       +   -    （二元    加减运算符）
|       <   <=  >   >=
|       ==  !=
|       and
|       or
低       =   +=  -=  *=  /=  //= %=
"""
