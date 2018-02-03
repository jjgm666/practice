# 对象和类
# 1.定义类
import math
class Circle:
    def __init__(self,radius=1):
        self.radius=radius
    def getPerimerter(self):
        return 2 * self.radius * math.pi
    def getArea(self):
        return  self.radius*self.radius*math.pi
    def setRadius(self,radius):
        self.radius=radius

# 2.构造对象  :  类名（参数）
Circle()

# 3.访问对象成员
c1=Circle(5)
c2=Circle()
print(c1)
print(c2)
print("Area is:",Circle(5).getArea())

"""
def Class_1:
    def __init__(self , ...)
        self.x = 1    创建 self.x 作用域为整个Class_1
        ...
    def m1(self , ...)
        self.y = 2    创建 self.y 作用域为整个Class_1,但m1中赋值为2
        ...
        z = 5         创建 z 作用域为m1
        ...
    def m2(self , ...)
        self.y = 3    创建 self.y 作用域为整个Class_1,但m1中赋值为3
        ...
        u = self.x + 1  创建 u 作用域为m2
        self.m1(...)

"""

# 4.使用类
from TV import TV

def main():
    tv1 = TV()
    tv1.turnOn()
    tv1.setChannel(30)
    tv1.setValume(3)

    tv2=TV()
    tv2.turnOn()
    tv2.channelUp()
    tv2.channelUp()
    tv2.volumeUp()

    print("tv1's channel is:",tv1.getChannel(),"and volume level is",tv1.getVolumeLevel())
    print("tv2's channel is:", tv2.getChannel(), "and volume level is", tv2.getVolumeLevel())

main()

# 隐藏数据域
"""
私有数据域定义： 仅可在类内部访问，类外部不可访问
    __privateName
    
    用get方法，让客户端访问数据域
        def getRadius(self):
            return self.__radius
    用set方法，为私有数据设置一个新值
"""