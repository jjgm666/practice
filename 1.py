#format字符串
age = "3"
name = "Tom"
print("{0} was {1} years old".format(name,age))
#

#字符串的连接   +
print(name + " was " +str(age) + " years old")
#
#程序自带数据
width = 5.5
height = 2
print("area is",width * height)
#

#从控制台读取输入(输入的是一个字符串，    可以用  eval()   函数   将其转换为  数值型！！
radius = eval(input("Enter a value for radius:"))
area = radius * radius * 3.14159
print("The area for the circle of radius",radius,"is:",area)
#

#交换两个参数的值
x = 1
y = 2
x , y = y , x
print(x,y)
#

#多值输入
number1 , number2 , number3 = eval(input("Enter three numbers separated by commas:"))
average = (number1 + number2 + number3) /3
print("The average of", number1 , number2 , number3 , "is" , average)
#

#运算符——   +  -  /  //  **   %
a = 1 + 2
b = 1 - 2
c = 1 * 2
d = 1 / 2
e = 1 // 2
f = 4 ** 2
g = 20 % 3

print("加法a=",a,",减法b=",b,"乘法c=",c,",除法d=",d,",取整e=",e,",求幂f=",f,",取余(取模)g=",g)
#

#以秒计时的一段时间转换为以分和秒计时的时间
seconds = eval(input("输入一个以秒计时的一段时间："))
minutes = seconds // 60
newseconds = seconds % 60
print(seconds,"转换成",minutes,"分",newseconds,"秒")
#

#科学记数法
#1.23456E2   123.456E-2

#增强运算符
'''
a+=4    a=a+4
a-=4    a=a-4
a*=4    a=a*4
a/=4    a=a/4
a//=4   a=a//4
a%=4    a=a%4
a**=4   a=a**4
'''
#

#类型转换   四舍五入
value = 5.6
a = int(value)
b = round(value)
c = round(5.2)
print(a,b,c)
#

#营业税保留两位小数
purchaseAmount=eval(input("输入营业额："))
tax=purchaseAmount*0.06
print("营业税为",int(tax*100)/100.0)  #保留了两位小数
#

#显示当前时间
import time

currrntTime = time.time()
totalSeconds = int(currrntTime)
nowSeconds = totalSeconds % 60
totalMinutes = totalSeconds // 60
nowMinutes = totalMinutes % 60
totalHours = totalMinutes // 60
nowHours = totalHours % 24
print("现在时间：",nowHours,"时",nowMinutes,"分",nowSeconds,"秒")
#

