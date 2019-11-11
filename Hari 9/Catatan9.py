'''
Job Connector Data Science
Purwadhika Startup & Coding School
Senin, 4 November 2019

C A T A T A N
'''

## LAMBDA FUNCTION ##

X = lambda a : a 

'''
x = variabel
lambda = function
a = parameter (anonymous)
: = bagi
a = return
'''
x = lambda a : a
print(x(2))
print(type(x)) # untuk mengetahui type dari x

# lambda memiliki fungsi yang sama dengan def
def y(a):
    return a
print(y(4))

# lambda bermanfaat ketika membuat function dalam function.

''' 
x = lambda a,b,c : a+b+c
def  y(a, b, c):
    return a+b+c
print(x(2,3,4))
print(y(2,3,4))
'''

# Lambda Pangkat function

def myFunction(x):
    return lambda a : a ** x

pangkat2 = myFunction(2)
pangkat3 = myFunction(3)
pangkat4 = myFunction(4)

print(pangkat4(6))
print(pangkat3(8))

'''fungsi lambda myFunction dalam def bergunan untuk mempangkatkan parameter berdasarkan variable.
hanya saja permsalahannya hanya satu expression.
'''


# Lambda If & Else

s = lambda a : True if a % 2 == 0 else False

def m(a):
    if a % 2 == 0:
        return True
    else:
        return False

print(x(4))
print(y(4))

x = lambda a : 'Angka Genap' if a % 2 == 0 else 'Angka Ganjil'
x = lambda a : print(a)
x('Hello') # cara ngeprint yang benar
print(x('Hello')) # pasti none, prinsip dasar return function


# Function Map
'''map python berfungsi untuk mengetahui dan mengeksekusi 
spesifik function tertentu dalam variable.'''

def r(a):
    return len(a)
a = ['Andilala', 'BudiCaca', 'Caca']
x = map(r, a)
print(x)
print(list(x))

# menggunakan function map melalui def
a = ['coklat', 'melon', 'nangka']
b = ['apel', 'jeruk', 'nanas']

def combi(a, b):
    return a+' '+b
x = map(combi, a, b)
print(x)
print(list(x))

x = [2, 4, 6, 8, 10]
def pangkat6(a):
    return a ** 2
y = map(pangkat6, x)
print(list(y))
# out = [4, 16, 36, 64, 100]

# menggunakan lambda
x = [2, 4, 6, 8, 10]
z = map(lambda a : a ** 2, x)
print(list(z))

# lambda 1 baris
print(list(map(lambda a : a ** 2, [2, 4, 6, 8, 10])))

# menggunakan append
x = [2, 4, 6, 8, 10]
b =[]
for i in x:
    b.append(i ** 2)
print(b)


# FILTER

x = range(11)
print(list(x))

# menggunakan def
x = range(11)
def kurangLima(x):
    if x < 5:
        return False
    else:
        return True
y = filter(kurangLima, x)
print(list(y))

# menggunakan lambda function
z = filter(lambda a: True if a >= 5 else False, x)
print(list(z))

# menggunakan power
x = pow(2, 3)
y = pow(3, 3)
print(x)
print(y)

# atau menggunakan function map
z = list(map(pow, [2, 3], [3, 3]))
print(z)

# menggunakan lambda
x = [1, 2, 3, 4, 5]
y = [1, 2, 6, 7, 8]
z = list(filter(lambda a: a in x, y))
print(z)

# menggunakan boolean
x = [1, 2, 3, 4, 5]
y = [1, 2, 6, 7, 8]
z = list(filter(lambda x: True if x <3 else False, x))
print(z)

# menggunakan loop for
x = [1, 2, 3, 4]
hasil = 1
for i in x:
    hasil *= i
print(hasil)


# REDUCE
angka = [1, 2, 3, 4]
hasil = 1
for i in angka:
    hasil *= i
print(hasil)

from functools import reduce
z = reduce(lambda x, y: x * y, angka)
print(z)


kata = ['Ini', 'Ibu', 'Budi']
print(''.join(kata))

from functools import reduce
z = reduce(lambda x, y: x+y, kata)
print(z)

angka = [1, 2, 3, 4]

# filter dalam map
z = list(map(lambda x : x* 2, filter(lambda x: x>3, angka)))
print(z)

# map dalam filter
z = list(filter(lambda x: x>3, map(lambda x : x*2, angka)))
print(z)

angka = list(range(1, 100))
print(angka)