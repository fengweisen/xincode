'''
r=input("")
c=3.1415*r*2
print("{:.0f}".format(c))

def func(a,*b):
    for item in b:
        a+=item
    return a
m=0
print(func(m,1,1,2,3,5,7,12,21,33))

txt=open('demo.txt','r')
print(txt)
txt.close

def func (num):
    num*=2
x=20
func(x)
print(x)


n=2
def multiply(x,y=10):
    global n
    return x*y*n
s=multiply(10,2)
print(s)


def fun(ss,x=2.0,y=4.0):
    ss+=x*y
ss=10
print(ss,fun(ss,3))

f1=1.01e4
print(f1)
num=5+4j
print(num.real)
print(num.imag)

print('nihao')
print("hello")
print("""111
222
333
""")

a=123
print(type(a))

age="16"
print(type(age))
age_new=int(age)
print(int(age_new))

m=4.5
print(type(m))
m1=int(m)
print(m1)

a=12 +34j
print(a.imag)

x=10
y=-1+2j
print(x+y)

x=3
y=4
print(x/y)
print(x//y)

s1="ni"
s2="hao"
i=23
print(s1+s2)
i2=str(i)
print(s1+i2)

a=5
b=3
a,b =b,a
print(a,b)
print(b)

x=y=123
a=b=c="helloword"
print(x,y)
print(a,b,c)

age=input("年龄：")
print("年龄："+age)
age1=int(age)+10
print("新的年龄",+age1)

score=58
if score >=60:
    print("及格")

password=555
if password ==123456:
    print("正确")
else:
    print("错误")

amount=1000
a=eval(input("取款金额:"))
if a<=amount and a%100==0:
    print("请输入金额")
else:
    print("穷鬼")

s=eval(input(""))
if s<60:
    print("不及格")
elif s>60 and s<80:
    print("及格")
else:
    print("优秀")

i=0
while(i<=10):
    print("helloword")
    i=i+1

i=1
while (i<100):
    print(i,end="\n")
    i=i+2

s=0
i=1
while(i<=100):
    print(s)
    s = s + i
    i=i+1

count=0
i=1
while(i<100):
    i=i+1
    if i%2==1:
        continue
    print(i)
    count+=1
    if count==3:
        break

def fun():
    s=0
    i=1
    while(i<=100):
        s=s+i
        i=i+1
    print(s)
fun()

def add(a,b):
    return(a+b)
s=add(3,4)
print(s)

def fun(a,b):
    return b,a

m,n=fun(3,4)
print(m,m)

def fun(a):
    a=5
    print(a)

m=10
fun(m)
print(m)


def fun1():
    sum = 0  # 初始化一个变量 sum 用于累加求和
    i = 1    # 初始化一个变量 i 作为循环的计数器，从 1 开始

    while i <= 100:  # 使用 while 循环，当 i 小于等于 100 时循环
        sum = sum + i  # 将 i 的值加到 sum 上
        i = i + 1      # 将 i 的值增加 1

    print(sum)  # 打印最终的累加结果
fun1()

def fun2():
    sum=0
    i=1
    while i <= 100:  # 使用 while 循环，当 i 小于等于 100 时循环
        sum = sum + i  # 将 i 的值加到 sum 上
        i = i + 1      # 将 i 的值增加 1
    return sum
print(fun2())

s=eval(input(""))
def fun3(s):
    if s>60:
        print("及格")
    else:
        print("不及格")
fun3(s)

s=eval(input(""))
def fun3(s):
    if s>60:
        return 1
    else:
        return 0
print(fun3(s))

def fun():
    a=10
    b=15
    print(a,b)
fun()

n=5
def fun():
    a=10
    b=15
    print(a,b)
    print(n)
fun()

n=2
def fun(a,b):
    global n
    n=a+b
    print(n)
fun(5,6)
print(n)

print(26,end="^^")

s1="nihaio"
s2=5
print(s1*s2)

s1="nihao"
print("n"in s1)
s2="hao"
print(s2 in s1)

s="hao are you"
print(s[0])
print(s[1:6])
print(s[1:])
print(s[:8])
print(s[0:7:2])

s="abcdefg"
print(s[::-1])
print(s[-1])
print(s[:-2])

s="hao are you doing"
for i in s:
    print(i)

s=1
print(chr(s))
print(ord(s))

a=123
print(hex(a))
print(oct(a))

s="abBhU"
print(s.upper())

s="a-bhj-b-ki-loj"
a=s.split("-")
print(s)

s="jdianoihaiochakojnduiahwncxiaon"
print(s.count("a"))

s1="hello ojuk koij"
s2=s1.replace("o","A")
print(s1)
print(s2)

s="abc"
print(s.center(10,"="))
print(s.center(10,"="))

s1="      ===jikl      "
print(s1.strip(" ="))

print(",".join("python"))

s1="hello world ni hao"
print(s1.capitalize())

s1="i am a big boy in a big worlg"
print(s1.index("g"))
print(s1.find("girl"))
print(s1.find("g",25,27))

print("{}说，今天天气不错".format("张三"))
print("{}说，今天是个{}日子".format("张三","好"))

s="123"
print("{:25}".format(s))
print("{:2}".format(s))
print("{:>25}".format(s))
print("{:*^25}".format(s))

s="二级考试"
y="+"
print("{0:{1}^25}".format(s,y))

print("{:-^25,}".format(25286))

print("{0:e},{0:E},{0:f},{0:%}".format(25.32))

s={123,252,265,"123","asd","abc"}
print(s)

s={123,456,7989,"asd","bhj"}
t={123,456,"wsx"}
print(s-t)
print(s^t)
print(s&t)
print(s|t)
print(len(s))
s=s.add(123)
print(s)

s=set({})
print(s)

s=[12323,123,123,"abc","abc"]
print(s)
print(type(s))
print(s[0])

s={"101":"zhangsan","102":"lisi","103":"wamgwu","104":"zhaoliu"}
print(s.keys())
print(type(s.keys()))
print(s.values())
print(s.items())
for i in s:
    print(i)
for i in s.values():
    print(i)

for i in s.items():
    print(i)
for k,v in s.items():
    print(k,v)


s={"101":"zhangsan","102":"lisi","103":"wamgwu","104":"zhaoliu"}
print(s.get(("101")))
print(s["101"])
s.pop("101")
print(s)
print(s.popitem())
print(s)

f=open("data.txt","r",encoding="utf_8")
s=f.read()
f.close()
print(s)

path="data.txt"

print("hello\tword")

from conda.auxlib.compat import utf8_writer

path="data.txt"
f=open(path,"r",encoding="utf_8")
a=f.read()
f.close()
print(a)

from idlelib.iomenu import encoding

path="data.txt"
f=open(path,"r",encoding=="utf_8")
s=f.read(4)
f.close()
print(s)

from docutils.parsers.rst.directives import encoding

path="data.txt"
f = open(path, "r", encoding="utf_8")
f.seek(0 )
s=f.readlines()
f.close()
print(s)

path="1.txt"
f=open(path,"w",encoding="UTF_8")
ls=["张三 \n","李四 \n","王五 \n","赵六 \n"]
f.writelines(ls)
f.close()

f=open("city.csv","r")
info=f.read()
ls=info.split(",")
f.close()
print(ls)

st=[
    ["学号","性别","年龄","姓名"],
    ["101","男","20","张三"],
    ["102","男","22","王五"],
    ["103","女","20","李四"]
]
f=open("st.csv","w")
for i in st:
    s=",".join(i)+"\n"
    f.write(s)
f.close()

f=open("st.csv","r")
for i in f:
    i=i.strip("\n")
    temp=i.split(",")
    print(temp)
f.close()

'''
def fun1():
    print("nihao")
def fun2():
    print("zhangsan")
def fun3():
    print("lisi")
def fun4():
    print("w")
