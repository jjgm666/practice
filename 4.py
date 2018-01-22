"""循环"""
# 1.while循环
count = 0
while count < 10:
    print("Python is fun!", count)
    count += 1

sum = 0
i = 1
while i < 10:
    sum = sum + i
    i += 1
print("sum is:",sum)

import random
number1 = random.randint(0,9)
number2 = random.randint(0,9)

if number1 < number2:
    number1,number2 = number2,number1

answer = eval(input("请输入下面式子的正确答案：\n"+ str(number1) + "+" + str(number2) + "="))

while answer != number1 + number2:
    print("答案错误，请重试！")
    answer = eval(input("请输入下面式子的正确答案：\n" + str(number1) + "+" + str(number2) + "="))
print("答案正确！")

print("······猜数字游戏(0~100)······")
number = random.randint(0,100)
guess = 0
while guess != number:
    guess = eval(input("请输入猜想的数字："))
    if guess > number:
        print("您猜的数大了！")
    elif guess < number:
        print("您猜的数小了！")
    else:
        print("您猜对了！")

# 输入输出重定向

