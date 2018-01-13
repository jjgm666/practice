#format字符串
age = "3"
name = "Tom"
print("{0} was {1} years old".format(name,age))

#字符串的连接   +
print(name + " was " +str(age) + " years old")

#程序自带数据
width = 5.5
height = 2
print("area is",width * height)


#从控制台读取输入(输入的是一个字符串，可以用eval函数将其转换为  数值型！！
radius = eval(input("Enter a value for radius:"))
area = radius * radius * 3.14159
print("The area for the circle of radius",radius,"is:",area)

#交换两个参数的值
x = 1
y = 2
x , y = y , x
print(x,y)

#多值输入
number1 , number2 , number3 = eval(input("Enter three numbers separated by commas:"))
average = (number1 + number2 + number3) /3
print("The average of", number1 , number2 , number3 , "is" , average)