'''
Job Connector Data Science
Purwadhika Startup & Coding School
Senin, 28 Oktober 2019
'''

## FUNCTION ##

def hello():
    print('hello world!')


# f(x) = x ^ 2
def kuadrat(angka):
    print(angka ** 2)

# untuk memanggil fungsi
kuadrat(2)
kuadrat(3)


def gangen(x):
    if x % 2 == 0:
        print(x, 'tergolong GENAP')
    else:
        print(x, ) #

# .... sampe sini juga ........
'''

# sebuah function calc
# 1. masukkan angka : 10
# 2. masukkan operator aritmatika: +-/*  /
# 3. masukkan angka 5 : 5

# output : 
'''

def calc():
    x = float(input('masukkan angka 1 : '))
    op = input('masukkan operator (+-/*) : ')
    y = float(input('masukkan angka 2 : '))
    if op == '+' :
        print(x+y)
    elif op == '-' :
        print(x-y)
    elif op == '/' :
        print(x/y)
    elif op == '*' :
        print(x*y)
    else:
        print('maaf operator tidak dikenali')
calc()

students = ['Andi', 'Budi', 'Caca']

def tes(x) :
    print(x[0])
    print('Caca' in x)

tes(students)


# ubah huruf vokal => 0
# function untuk mereplace huruf

def vocal(kalimat):
    kalimat = kalimat.lower()
    kalimat = kalimat.replace('a','o')
    kalimat = kalimat.replace('i','o')
    kalimat = kalimat.replace('u','o')
    kalimat = kalimat.replace('e','o')
    kalimat = kalimat.replace('o','o')
    print(kalimat)

vocal('Selamat DAtang')
vocal('kantal')

# if statement
# function

# Return function

def LuasPersegi(sisi):
    print(f' Luas = {sisi*sisi}')
def LuasPersegiReturn(sisi):
    return sisi * sisi

LuasPersegi(5)
# Return berfungsi untuk menyimpan value

## WHILE LOOP ##

while True:
    print('True')

i = 20
while i >= 1:
    print(i)
    i -= 1

students = ['Andi', 'Budi', 'Caca', 'Deni']
index = 0
while index <= len(students) -1 :
    print(students[index])
    index += 1

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = []
index =0
while index <= len(x)-1:
    y.append(x[index] ** 2)
    index += 1
print(y)

# break and continue

i = 1
while i < 50:
    print(i)
    if i == 5:
        break
    i += 1
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)


password = '12345'
input('ketik password : ')
input('password salah! ketik password : ')
input('password salah! ketik password : ')
input('password benar!')


inputuser = ''
while inputuser != password:
    inputuser = input('ketik password : ')
    if inputuser != password: 
        print('password salah!')
    else:
        print('password benar!')

password = '12345'
inputuser = ''
jumlahinput = 0
batasinput = 5
lebih = False

while inputuser != password and not lebih:
    if jumlahinput < batasinput:
        inputuser = input(f'input ke-{jumlahinput} ketik password! : ')
        jumlahinput += 1
    else:
        lebih = True

if lebih:
    print('kesempatan sudah habis, tunggu 24 hari su')
else:
    print('password benar!')


P = []
Q = []
R = []
S = []

for i in range(-4, 5, 1):
    Q.append(i)

for i in range(-7, 1, 1):
    R.append(i)

for i in range(-1, 8, 1):
    S.append(i)

for i in range(-9, 10, 1):
    P.append(i)

print(sorted(set(P)))
print(sorted(set(Q)))
print(sorted(set(R)))
print(sorted(set(S)))