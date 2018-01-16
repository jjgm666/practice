#常见的python函数
'''
使用时直接使用函数名即可
abs(x)   取绝对值
max(x1,x2,..,xn)   取最大值
min(x1,x2,..,xn)   取最小值
pow(a,b)  返回a^b,相当于a**b
round(x)   返回与x最接近的整数，若两个整数都与x接近，则返回偶数值
round(x,b)   保留小数点后n位小数的浮点值

使用时应为  math.函数名(a)
fabs(x)    将x看作是一个浮点数，并返回其绝对值
ceil(x)    向上取整
floor(x)    向下取整
exp(x)     返回幂函数e^x的值
log(x)     返回x的自然对数值
log(x,base)     返回以某个特殊值base为底的x的对数值
sqrt(x)    返回x的平方根
degrees(x)   将x从弧度转换为角度
radians(x)   将x从角度转换为弧度
sin(x)   cos(x)    asin(x)   acos(x)  tan(x)   三角函数

pi   常数π
e    常数e

使用这些数据和常数   需要事先导入 math  包
'''

#字符串和字符
import turtle
turtle.write("\u6B22\u8FCE\u03b1\u03b2\u03b3")
turtle.done()

#函数   ord(ch) 用于返回字符ch的ASCII码  和   chr(code)用于返回code所编码的字符
ch='A'
print(ord(ch))
print(chr(102))

#转义序列
'''
\b 退格符
\f 制表符
\n 换行符
\f 换页符
\r 回车符
\\ 反斜线\
\' 单引号’
\" 双引号“
'''
print("He said,\"I love you！\"")

#不换行打印    调用print时传递一个特殊参数  end="任意一个字符串"
print("AAA",end="abcd")
print("BBB",end="    ")
print("CCC",end="efgh")

#函数str()  将一个数字转换成字符串
#如  str(3.4)  为   '3.4'

#字符串的连接操作  用  +   以及  += 均可 进行
message = "\nWelcome " + "to " + "Python "
print(message)

message += "and Python is fun!"
print(message)

#从控制台读取字符串   用  inout()  函数
s1 = input("Enter a string:")
s2 = input("Enter a string:")
s3 = input("Enter a string:")
print("s1 is " + s1)
print("s2 is " + s2)
print("s3 is " + s3)
