'''
    belajar dari awal berdasarkan 
    materi
    yang ada di powerpoint


x = 5
y = '5'

print(x == y)
print(x > int(y))
print(x >= int(y))
print(x < int(y))
print(x <= int(y))

x = 5
y = '5'
z = 6

print(x==int(y) and int(y)<z)
print(x==int(y) or int(y)<z)
print(not(x==int(y) or int(y)<z))
'''

# if, elif & else

'''
nilai = 40

if (nilai > 80):
    print('excellent!')
elif (nilai >= 60 and nilai <= 80):
    print('Goodjob!')
else :
    print("Don't give up!")

nilai = 80

if (nilai > 80):
    print('excellent!')
elif (nilai >= 60 and nilai <= 80):
    print('Goodjob!')
else :
    print("Don't give up!")

nilai = 100

if (nilai > 80):
    print('excellent!')
elif (nilai >= 60 and nilai <= 80):
    print('Goodjob!')
else :
    print("Don't give up!")

jomblo = True

if (jomblo):
    print('Masih jomblo!')
else :
    print('Udah taken!')

jomblo = False

if (jomblo):
    print('Masih jomblo!')
else :
    print('Udah taken!')
'''

# LOOP

''' 1. While Loop '''
'''
angka = 1 

while(angka <= 10):
    print(angka)
    angka += 1
'''
''' For Loop and List '''
'''
list_item = list(range(1, 11, 2))
print(list_item)

for item in range(1,11,2):
    print(item)
'''

for i in range(1,11): 
    print('*')

for i in range(1,11):
    print('*'*10)

for i in range(1,11):
    print('*'*(11-i))

for i in range(1,11):
    print('x'*i)

for i in range(10,0,-1):
    print(' '*(i-1) + '*'*(11-i))

for i in range(10,0,-1):
    print(' '*(i-1) + '*'*(11-i)+'*'*(10-i))







