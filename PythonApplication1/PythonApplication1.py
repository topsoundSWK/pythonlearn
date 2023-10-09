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
        L = [L[i-1] + L[i] for i in range(len(L))] #根据上一行的列表元素生成当前行
        
n = 0
for t in triangles(10):
    print(t)
    n=n+1
    if n == 10:
        break