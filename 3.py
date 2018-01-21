# 选择

# 布尔表达式、数值表达式
radius = 1
print(radius > 0)
print(radius < 0)
print(int(radius > 0))
print(int(radius < 0))

# 产生随机数  random()函数,需要引入random包,用法是：random.randint(a , b)
import random

number1 = random.randint(0,20)
number2 = random.randint(0,20)
answer = eval(input("What is " + str(number1) + "+" +str(number2) + "?"))
print(number1,"+",number2,"=",answer,"is",number1+number2==answer)