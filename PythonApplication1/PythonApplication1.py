count = 1
sum = 0
while count <= 100:
    if(count % 2 == 0):
        count = count + 1
        continue
    sum = sum + count
    count = count + 1
print (sum)

for num in range(10, 20):   #遍历10-19
    for i in range(2, num): #如果num能被整除
        if num % i ==0:
            #j = num/i
            print('%d 是一个合数' % num)
            break
    else:
        print('%d是一个质数' % num)
        
for i in range(1, 10):  #1-9
    for j in range(1, i +1): #1到当前值
        print('{}x{}={}\t'.format(i,j,i*j), end='') 
    print()
    
year = int(input("请输入一个年份："))
if(year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
    print('{0}是闰年'.format(year))
else:
    print('{0}不是闰年'.format(year))
    

def sum(num1,num2):
	# 两数之和
	if not (isinstance (num1,(int ,float)) and isinstance (num2,(int ,float))):
		raise TypeError('参数类型错误')
	return num1+num2
print(sum(1,"3"))

def division(num1, num2):
    a = num1 % num2
    b = (num1 - a) / num2
    return b, a

num1, num2 = division(9,4)
tuple1 = division(9,4)
print (num1, num2)
print (tuple1)

#默认参数
def printer(name, age, sex = '男'):
    print('昵称：{}'.format(name), end=' ')
    print('年龄：{}'.format(age) , end=' ')
    print('性别：{}'.format(sex))
    return
printer('两点水' , 18 , '女')
printer('swk', 26, "male")

def print_user_info(name, age, sex="male", **hobby):
    print("昵称:{}".format(name), end=' ')
    print("年龄:{}".format(age), end=' ')
    print("性别:{}".format(sex), end=' ')
    print("爱好:{}".format(hobby))
    return;

print_user_info(name = '两点水' , age = 18 , sex = '女', hobby = ('打篮球','打羽毛球','跑步'))

def print_user_info( name , *, age  , sex = '男' ):
    # 打印用户信息
    print('昵称：{}'.format(name) , end = ' ')
    print('年龄：{}'.format(age) , end = ' ')
    print('性别：{}'.format(sex))
    return;

print_user_info( name = '两点水' ,age = 18 , sex = '女' )

def change_number(b):
    print('函数中一开始 b 的值：{}' .format( b ) )
    b = 1000
    print('函数中 b 赋值后的值：{}' .format( b ) )
    
b = 1
change_number(b)
print(b)

def change_list(b):
    print('函数中一开始 b 的值：{}' .format( b ) )
    b.append(1000)
    print('函数中 b 赋值后的值：{}' .format( b ) )


b = [1,2,3,4,5]
change_list( b )
print( '最后输出 b 的值：{}' .format( b )  )

#匿名函数
sum = lambda num1, num2 : num1+num2;
print(sum(1, 2))

#迭代
for char in 'songwenke':
    print(char, end = ' ')
    
print('\n')

dict1 = {'name':'两点水','age':'23','sex':'男'}
for key in dict1 :    # 迭代 dict 中的 key
    print ( key , end = ' ' )

print('\n')
for value in dict1.values() :   # 迭代 dict 中的 value
	print ( value , end = ' ' )

print ('\n')

for x , y in [ (1,'a') , (2,'b') , (3,'c') ] :
	print ( x , y )
    
    
str1 = 'songwenke'
iter1 = iter(str1)

list1 = [1,2,3,4]
iter2 = iter(list1)

tuple1 = (1,2,3,4)
iter3 = iter(tuple1)

for x in iter1:
    print(x, end=' ')
print('\n---------')

while True:
     try:
         print(next(iter3)) 
     except StopIteration:
         break
     
list1 = list(range(1, 31))
print(list1)

print('\n'.join([' '.join ('%dx%d=%2d' % (x,y,x*y)  for x in range(1,y+1)) for y in range(1,10)]))

list1 = [x*x for x in range(1,11)]
print(list1)

list1 = [x*x for x in range(1, 11) if x % 2 == 0]
print(list1)

list2 = [(x+1,y+1) for x in range(3) for y in range(5)]
print(list2)

#生成器generator
gen = (x*x for x in range(10))
print(gen)

'''
生成器表达式使用了“惰性计算” ( lazy evaluation，
也有翻译为“延迟求值”，我以为这种按需调用 call by need 的方式翻译为惰性更好一些)，
只有在检索时才被赋值（ evaluated ），所以在列表比较长的情况下使用内存上更有效。
生成器并不真正创建数字列表， 而是返回一个生成器，这个生成器在每次计算出一个条目后，把这个条目“产生” ( yield ) 出来。
'''
gen= (x * x for x in range(10))
for num in gen:
    print (num) 
    
def my_func():
    for i in range(10):
         print(i, end=" ")
         
my_func()

def myfunc():
    for i in range(10):
         yield i
         
print(myfunc())

def fib(n):
    a=b=1
    for i in range(n):
        yield a
        a, b = b, a+b
        
for x in fib(1000000):
    print (x, end=' ') 
    
def odd():
    print('step1')
    yield(1)
    print('step2')
    yield(3)
    print('step3')
    yield(5)
    
o = odd()
print(next(o))
print(next(o))
print(next(o))

#生成器生成杨辉三角
def triangles(n):
    L = [1]     #初始化列表L为[1]
    while True:
        yield L #yield 语句将当前的列表 L 返回，并且函数的执行状态会被暂停。下次迭代时，函数会从上次暂停的地方继续执行，生成下一个列表 L。
        L.append(0) #先累加一个0
        L = [L[i-1] + L[i] for i in range(len(L))] #根据当前行的列表生成下一行，注意：L[-1]为L中的最后一个元素，即累加的0
        
n = 0
for t in triangles(10):     #遍历 triangles(10)
    print(t)                #打印每个生成的列表
    n=n+1                   #计数
    if n == 10:             #10行结束打印
        break
    
#生成器生成杨辉三角，上一版本传入的参数并未用上
def triangles():
    L = [1]     #初始化列表L为[1]
    while True:
        yield L #yield 语句将当前的列表 L 返回，并且函数的执行状态会被暂停。下次迭代时，函数会从上次暂停的地方继续执行，生成下一个列表 L。
        L.append(0) #先累加一个0
        L = [L[i-1] + L[i] for i in range(len(L))] #根据当前行的列表生成下一行，注意：L[-1]为L中的最后一个元素，即累加的0
        
n = 0
for t in triangles():     #遍历 triangles(10)
    print(t)                #打印每个生成的列表
    n=n+1                   #计数
    if n == 10:             #10行结束打印
        break
    
#迭代器和生成器综合例子，两者基本互通
List1 = [1,2,3,4,5]
for num in List1:
    print(num, end=' ')
    
List1 = [1,2,3,4,5]
for num in reversed(List1):
    print(num, end=' ')
    
class Countdown:        #Countdown自定义类
    def __init__(self, start):  #初始化一个对象
        self.start = start  #倒计时的起始值
        
    def __iter__(self):#定义正向迭代器
        #fwd
        n = self.start
        while n > 0:    #递减
            yield n     #每次yield一个值
            n -= 1
            
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n 
            n += 1
            
for rr in reversed(Countdown(30)):
    print(rr)
    
for rr in Countdown(30):
    print(rr)
    
#同时迭代多个序列
names = ['sadadde', 'swk', 'songwenke']
ages = [12,34,54]
for name, age in zip(names, ages):
    print(name, age)
    
#利用zip(),生成dict

names = ['sadadde', 'swk', 'songwenke']
ages = [12,34,54]

dict1 = dict(zip(names, ages))
print(dict1)

#Class
class ClassA:
    var1 = 100
    var2 = 0.01
    var3 = 'swk'
    
    def func1():
        print('I`m swk1')
    
    def func2():
        print('swk2')
    
    def func3():
         print('swk3')
    
print(ClassA.var1)
print(ClassA.var2)
print(ClassA.var3)
ClassA.func1()
ClassA.func2()
ClassA.func3()

#方法调用属性
class A():
    var1 = 'swk'
    
    @classmethod
    def func1(cls, age):
        print('我是 func1' + cls.var1)
        print('Nianji' + str(age))
        
A.func1(18)

#修改类属性
class A:
    a='swk'
    
    @classmethod
    def func(cl):
        print('before:' + cl.a)
        cl.a = input('input here')
        print('now a is:' + cl.a)
        cl.b = input('add b: ')
        print('b为：' + cl.b)
        
A.func()

#类的外部修改属性
class B:
    var1 = 'songwenke'
    
    @classmethod
    def func(cls):
        print('var1:' + cls.var1)
        
B.func()
B.var1 = input('输入要修改的值')
B.func()

B.var2 = input('输入v2')
print(B().var2)

#类和对象
class ClassA(object):
    var1 = '两点水'

    def fun1(cls):
        print('var1 值为：' + cls.var1)

a = ClassA()
a.fun1()
print(a.var1)

#构造函数
class cla:
    def __init__(self): #参数一定要是self
        print('swk')
        
a = cla()

#传参
class B(object):
    m_str = None
    def __init__(self, str):
        print('实例化成功')
        m_str = str
        print(str)
        print(m_str)
a = B('swkniubi')

#析构
class A(object):
    def __init__(self):
        print('gouzao')
        
    def __del__(self):
        print('~~~')
        
a = A()
del a

'''
class oldClass:
    pass
    
class newClass(object):
    pass  
'''

class oldClass:
    def __init__(self, account, name):
        self.account = account
        self.name = name
        
class newClass(object):
    def __init__(self, account, name):
        self.account = account
        self.name = name
        
if __name__ == '__main__':
    old_class = oldClass(111111, 'OldClass')
    print(old_class)
    print(type(old_class))
    print(dir(old_class))
    print('\n')
    new_class = newClass(222222, 'NewClass')
    print(new_class)
    print(type(new_class))
    print(dir(new_class))