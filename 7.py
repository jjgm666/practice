# 更多字符串和特殊方法
#1.字符串处理函数
s="Welcome"
len(s)  #求s的长度
max(s)  #求s中ASCII码最大的字符
min(s)  #求s中ASCII码最小的字符

#2.下标运算符
for i in range(0,len(s),2):
    print(s[i],end='')

#3.截取运算符[start : end]
s[1:4]

#3. 连接运算符+ 和 复制运算符*
s1 ="Welcome"
s2 ="Python"
s3 =s1 + " to " +s2
print("\n",s3)
s4= 6*s1
s5= s1*6
print(s4,"\n",s5)

#4.in和not in运算符
print("come" in s1)
print("come" not in s1)

#5.迭代字符串
for i in range(0,len(s),2):
    print(s[i]) #输出奇数位的字符

#6.测试字符串
s1="welcome to python"
s2="Welcome"
s3="2012"
s4="first number"
s5="a b c"

print("1.字符串",s1,"中的字符是字母或数字且至少有一个字符/t",s1.isalnum())
print("2.字符串",s2,"中的字符是字母且至少有一个字符/t",s2.isalpha())
print("3.字符串",s3,"中的字符只含有数字字符/t",s3.isdigit())
print("4.字符串",s4,"中的字符是Python标识符/t",s4.isidentifier())
print("5.字符串",s1,"中的字符是全是小写且至少有一个字符/t",s1.islower())
print("6.字符串",s1,"中的字符是全是大写且至少有一个字符/t",s1.isupper())
print("7.字符串",s5,"中的字符只包含空格/t",s5.isspace())

#7.搜素子串
sz="welcome to pyton"
s1="thon"
s2="good"
s3="come"
s4="become"
s5="o"
print("1.字符串",sz,"中的字符是以子串",s1,"为结尾的/t",sz.endswith(s1))
print("2.字符串",sz,"中的字符是以子串",s2,"为开始的/t",sz.startswith(s2))
print("3.字符串",sz,"中的字符中含有字符串",s3,"且返回其最低下标/t",sz.find(s3),"\t否则返回-1")
print("4.字符串",sz,"中的字符中含有字符串",s3,"且返回其最低下标/t",sz.find(s4),"\t否则返回-1")
print("5.字符串",sz,"中的字符中含有字符串",s4,"且返回其最高下标/t",sz.rfind(s5),"\t否则返回-1")
print("6.字符串",sz,"中的字符是全是小写且至少有一个字符/t",sz.count(s5))

#8.转换字符串
sz="welcome to pyton"
s1="New England"
s2="Amarica"
s3="England"

print("1.复制字符串",sz,"并将字符串中第一个字符大写",sz.capitalize())
print("2.复制字符串",s1,"并将字符串中所有字符转为小写",s1.lower())
print("3.复制字符串",sz,"并将字符串中所有字符转为大写",sz.upper())
print("4.复制字符串",sz,"并将字符串中所有单词的首字母大写",sz.title())
print("5.复制字符串",s1,"并将字符串中小写字母转为大写，大写字母转为小写",s1.swapcase())
print("6.用新字符串",s2,"替代原字符串",s1,"中的",s3,"\t",s1.replace(s3,s2))

#9.删除字符串中的空格
s="  Welcome to Python\t"
print("返回去掉前端空白字符的字符串",s.lstrip())
print("返回去掉末端空白字符的字符串",s.rstrip())
print("返回去掉两端空白字符的字符串",s.strip())

#10.格式化字符串
s="Welcome"
print("返回在给定宽度域上居中的字符串副本：\n",s.center(11))
print("返回在给定宽度域上左对齐的字符串副本：\n",s.ljust(11))
print("返回在给定宽度域上右对齐的字符串副本：\n",s.rjust(11))
print("格式化一个字符串：\n",s.format())