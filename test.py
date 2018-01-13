#Just a test py
print("Welcome to python!")
print("Python is fun!")
print("Problem driven!")

print((10.5+2*3)/(45-3.5))

#test turtle
import turtle  #导入turtle绘图包
#绘制初始点
turtle.showturtle()
turtle.write("welcome to python")
#箭头向箭头方向移动100
turtle.forward(100)
#按照当前箭头方向向右旋转90°，颜色蓝色，长度50
turtle.right(90)
turtle.color("blue")
turtle.forward(50)
#按照当前箭头方向向右旋转90°，颜色绿色，长度100
turtle.right(90)
turtle.color("green")
turtle.forward(100)
#按照当前箭头方向向右旋转45°，颜色红色，长度50
turtle.right(45)
turtle.color("red")
turtle.forward(80)

#penup函数抬起笔
turtle.penup()
#turtle的goto语句，将箭头移至任何位置
turtle.goto(0,50)
#pendown函数放下笔
turtle.pendown()

#用circle函数绘制圆
turtle.color("purple")
turtle.circle(60)
#done函数使图像稳定输出
turtle.done()