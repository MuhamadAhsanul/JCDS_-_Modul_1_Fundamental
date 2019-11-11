'''
Job Connector Data Science
Purwadhika Startup & Coding School
Rabu, 23 Oktober 2019

C A T A T A N
'''

## METHOD & LIST ##

x = 12
x = 13

x = 2
x += 2   # x = x + 2
x -= 2   # x = x - 2
x *= 2   # x = x * 2
x /= 2   # x = x / 2

x = 'abcdefghijgklmgnopgqrstuvwgxyz'
print(x[::2]) #untuk mengambil huruf per karakter dengan kelipatan 2
print('g' in x) #untuk mengetahui apakah karakter dalam kurung berada dalam x
print('12' in x) #sama kayak diatas
print(x.count('g')) #untuk mencari huruf g dalam kalimat.


# List
x = ['Andi', 'Budi', 'Caca', 123, True]
print(x[len(x) - 1])
print(type('x[-1'))


days = [
    'Senin', 'Selasa', 'Rabu','Kamis', 'Jumat', 
    'Sabtu','Minggu'
 ]
now = 'sabtu'
week = 7
totalhari = 100
currentindex = days.index(now.lower())
hari =  (totalhari%week) + currentindex
if (hari >6):    
    hari -=7

print(f'Maka {totalhari} hari lagi adalah hari {days[hari]}')


hari = ['mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

hari[1] = 'Monday'
print(hari)

hari[0] = 'Monday'
print(hari)

hari.append('senin3') #menambahkan
print(hari)

hari.insert(6, 'senin3') #menyisipkan
print(hari)

hari.remove('senin3') #menghilangkan derdasarkan yang diinginkan
print(hari)

hari.pop() #menghilangkan list berdasarkan index
print(hari)

hari.pop(0) #menghilangkan list berdasarkan urutan kata
print(hari)

hari.sort() #mengacak-acak kata
print(hari)

hari.reverse()
print(hari)


# List []
x = [12,34,1,9,18]
x.sort()
print(x)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = x[::2].copy()
print(x)
print(y)
print(x + y)
print(y * 2)

z = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(z[1][1])

a = [ 1, 2, 3, 4, 5, 6, 3]
def cariIndex (list, i):
    return(x for x, y in enumerate() if y == i)

print(cariIndex(a, 3))


