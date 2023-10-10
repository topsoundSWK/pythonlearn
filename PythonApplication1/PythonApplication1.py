count = 1
sum = 0
while count <= 100:
    if(count % 2 == 0):
        count = count + 1
        continue
    sum = sum + count
    count = count + 1
print (sum)

for num in range(10, 20):   #����10-19
    for i in range(2, num): #���num�ܱ�����
        if num % i ==0:
            #j = num/i
            print('%d ��һ������' % num)
            break
    else:
        print('%d��һ������' % num)
        
for i in range(1, 10):  #1-9
    for j in range(1, i +1): #1����ǰֵ
        print('{}x{}={}\t'.format(i,j,i*j), end='') 
    print()
    
year = int(input("������һ����ݣ�"))
if(year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
    print('{0}������'.format(year))
else:
    print('{0}��������'.format(year))
    

def sum(num1,num2):
	# ����֮��
	if not (isinstance (num1,(int ,float)) and isinstance (num2,(int ,float))):
		raise TypeError('�������ʹ���')
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

#Ĭ�ϲ���
def printer(name, age, sex = '��'):
    print('�ǳƣ�{}'.format(name), end=' ')
    print('���䣺{}'.format(age) , end=' ')
    print('�Ա�{}'.format(sex))
    return
printer('����ˮ' , 18 , 'Ů')
printer('swk', 26, "male")

def print_user_info(name, age, sex="male", **hobby):
    print("�ǳ�:{}".format(name), end=' ')
    print("����:{}".format(age), end=' ')
    print("�Ա�:{}".format(sex), end=' ')
    print("����:{}".format(hobby))
    return;

print_user_info(name = '����ˮ' , age = 18 , sex = 'Ů', hobby = ('������','����ë��','�ܲ�'))

def print_user_info( name , *, age  , sex = '��' ):
    # ��ӡ�û���Ϣ
    print('�ǳƣ�{}'.format(name) , end = ' ')
    print('���䣺{}'.format(age) , end = ' ')
    print('�Ա�{}'.format(sex))
    return;

print_user_info( name = '����ˮ' ,age = 18 , sex = 'Ů' )

def change_number(b):
    print('������һ��ʼ b ��ֵ��{}' .format( b ) )
    b = 1000
    print('������ b ��ֵ���ֵ��{}' .format( b ) )
    
b = 1
change_number(b)
print(b)

def change_list(b):
    print('������һ��ʼ b ��ֵ��{}' .format( b ) )
    b.append(1000)
    print('������ b ��ֵ���ֵ��{}' .format( b ) )


b = [1,2,3,4,5]
change_list( b )
print( '������ b ��ֵ��{}' .format( b )  )

#��������
sum = lambda num1, num2 : num1+num2;
print(sum(1, 2))

#����
for char in 'songwenke':
    print(char, end = ' ')
    
print('\n')

dict1 = {'name':'����ˮ','age':'23','sex':'��'}
for key in dict1 :    # ���� dict �е� key
    print ( key , end = ' ' )

print('\n')
for value in dict1.values() :   # ���� dict �е� value
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

#������generator
gen = (x*x for x in range(10))
print(gen)

'''
���������ʽʹ���ˡ����Լ��㡱 ( lazy evaluation��
Ҳ�з���Ϊ���ӳ���ֵ��������Ϊ���ְ������ call by need �ķ�ʽ����Ϊ���Ը���һЩ)��
ֻ���ڼ���ʱ�ű���ֵ�� evaluated �����������б�Ƚϳ��������ʹ���ڴ��ϸ���Ч��
�����������������������б� ���Ƿ���һ���������������������ÿ�μ����һ����Ŀ�󣬰������Ŀ�������� ( yield ) ������
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

#�����������������
def triangles(n):
    L = [1]     #��ʼ���б�LΪ[1]
    while True:
        yield L #yield ��佫��ǰ���б� L ���أ����Һ�����ִ��״̬�ᱻ��ͣ���´ε���ʱ����������ϴ���ͣ�ĵط�����ִ�У�������һ���б� L��
        L.append(0) #���ۼ�һ��0
        L = [L[i-1] + L[i] for i in range(len(L))] #���ݵ�ǰ�е��б�������һ�У�ע�⣺L[-1]ΪL�е����һ��Ԫ�أ����ۼӵ�0
        
n = 0
for t in triangles(10):     #���� triangles(10)
    print(t)                #��ӡÿ�����ɵ��б�
    n=n+1                   #����
    if n == 10:             #10�н�����ӡ
        break
    
#����������������ǣ���һ�汾����Ĳ�����δ����
def triangles():
    L = [1]     #��ʼ���б�LΪ[1]
    while True:
        yield L #yield ��佫��ǰ���б� L ���أ����Һ�����ִ��״̬�ᱻ��ͣ���´ε���ʱ����������ϴ���ͣ�ĵط�����ִ�У�������һ���б� L��
        L.append(0) #���ۼ�һ��0
        L = [L[i-1] + L[i] for i in range(len(L))] #���ݵ�ǰ�е��б�������һ�У�ע�⣺L[-1]ΪL�е����һ��Ԫ�أ����ۼӵ�0
        
n = 0
for t in triangles():     #���� triangles(10)
    print(t)                #��ӡÿ�����ɵ��б�
    n=n+1                   #����
    if n == 10:             #10�н�����ӡ
        break
    
#���������������ۺ����ӣ����߻�����ͨ
List1 = [1,2,3,4,5]
for num in List1:
    print(num, end=' ')
    
List1 = [1,2,3,4,5]
for num in reversed(List1):
    print(num, end=' ')
    
class Countdown:        #Countdown�Զ�����
    def __init__(self, start):  #��ʼ��һ������
        self.start = start  #����ʱ����ʼֵ
        
    def __iter__(self):#�������������
        #fwd
        n = self.start
        while n > 0:    #�ݼ�
            yield n     #ÿ��yieldһ��ֵ
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
    
#ͬʱ�����������
names = ['sadadde', 'swk', 'songwenke']
ages = [12,34,54]
for name, age in zip(names, ages):
    print(name, age)
    
#����zip(),����dict

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

#������������
class A():
    var1 = 'swk'
    
    @classmethod
    def func1(cls, age):
        print('���� func1' + cls.var1)
        print('Nianji' + str(age))
        
A.func1(18)

#�޸�������
class A:
    a='swk'
    
    @classmethod
    def func(cl):
        print('before:' + cl.a)
        cl.a = input('input here')
        print('now a is:' + cl.a)
        cl.b = input('add b: ')
        print('bΪ��' + cl.b)
        
A.func()

#����ⲿ�޸�����
class B:
    var1 = 'songwenke'
    
    @classmethod
    def func(cls):
        print('var1:' + cls.var1)
        
B.func()
B.var1 = input('����Ҫ�޸ĵ�ֵ')
B.func()

B.var2 = input('����v2')
print(B().var2)

#��Ͷ���
class ClassA(object):
    var1 = '����ˮ'

    def fun1(cls):
        print('var1 ֵΪ��' + cls.var1)

a = ClassA()
a.fun1()
print(a.var1)

#���캯��
class cla:
    def __init__(self): #����һ��Ҫ��self
        print('swk')
        
a = cla()

#����
class B(object):
    m_str = None
    def __init__(self, str):
        print('ʵ�����ɹ�')
        m_str = str
        print(str)
        print(m_str)
a = B('swkniubi')

#����
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

#�̳�    
#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class UserInfo(object):
    lv = 5

    def __init__(self, name, age, account):
        self.name = name
        self._age = age
        self.__account = account

    def get_account(self):
        return self.__account

    @classmethod
    def get_name(cls):
        return cls.lv

    @property
    def get_age(self):
        return self._age


class UserInfo2(UserInfo):
    def __init__(self, name, age, account, sex):
        super(UserInfo2, self).__init__(name, age, account)
        self.sex = sex;


if __name__ == '__main__':
    userInfo2 = UserInfo2('����ˮ', 23, 347073565, '��');
    # ��ӡ��������
    print(dir(userInfo2))
    # ��ӡ���캯���е�����
    print(userInfo2.__dict__)
    print(UserInfo2.get_name())

#����������ж�
class User(object):
    pass
class User2(User):
    pass
class User3(User2):
    pass

if __name__ == '__main__':
    user1 = User()
    user2 = User2()
    user3 = User3()
    print(isinstance(user3, User2))
    print(isinstance(user3, User))
    print(isinstance(user3, User3))
    
    print(isinstance('����ˮ', str))
    print(isinstance(23453464, int))
    print(isinstance(24324355, str))
    
#��̬
class User(object):
    def __init__(self, name):
        self.name = name
        
    def printUser(self):
        print('hello!' + self.name)
        
class UserVip(User):
    def printUser(self):
        print('Hello! Vip�û�' + self.name)
        
class UserGeneral(User):
    def printUser(self):
        print('Hello! �𾴵��û�' + self.name)
        
def printUserInfo(user):
    user.printUser()
    
if __name__ == '__main__':
    userVip = UserVip('swk')
    printUserInfo(userVip)
    userGeneral = UserGeneral('SONGWENKE')
    printUserInfo(userGeneral)
 
    
#˽�з��������� �޶�
class UserInfo(object):
    def __init__(self, name, age, account):
        self.name = name
        self._age = age
        self.__account = account
        
    def get_account(self):
        return self.__account
    
if __name__ == '__main__':
    userInfo = UserInfo('songwenke', 26, 2209969938);

    print(dir(userInfo))
    print(userInfo.__dict__)
    print(userInfo.get_account())
    print(userInfo._UserInfo_account)
    
def _diamond_vip(lv):
    print('�𾴵���ʯ��Ա�û�������')
    vip_name = 'DiamondVip' + str(lv)
    return vip_name
def _gold_vip(lv):
    print('�𾴵Ļƽ��Ա������')
    vip_name = 'GoldVip' + str(lv)
    return vip_name
def vip_lv_name(lv):
    if lv ==1:
        print(_gold_vip(lv))
    elif lv == 2:
        print(_diamond_vip(lv))
        
vip_lv_name(2)