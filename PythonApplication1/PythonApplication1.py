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
for t in triangles(10):
    print(t)
    n=n+1
    if n == 10:
        break