'''
Job Connector Data Science
Purwadhika Startup & Coding School
Jumat, 1 November 2019

T U G A S
'''

# Soal ke 1 
def yNumber(x):
    number = ''
    for i in range(x):
        angka = 1 + i
        number += str(angka) + ' '
        print(number)
yNumber(5)

# Soal ke 2
def rNumber(x):
    number = ''
    for i in range(x):
        angka = x - i
        number = (str(angka) + ' ') * (x - i)
        print(number)
rNumber(5)

# Soal ke 3
def aNumber(x):
    number = ''
    for i in range(x):
        angka = 1 + i
        number = (str(angka) + ' ') * (1 + i)
        print(number)
aNumber(5)

# Soal ke 4
def bNumber(x):
    number = ''
    for i in range(x):
        angka = 1 + i
        number = (str(angka) + ' ') * (x - i)
        print(number)
bNumber(5)

# Soal ke 5
def cNumber(x):
    number = ''
    for i in range(x):
        angka = x - i
        number += (str(angka) + ' ')
        print(number)
cNumber(5)

# Soal ke 6
def dNumber(x):
    z = x + 1
    for i in range(1, z):
        number = ''
        for h in range(1, (z + 1 - i)):
            number += str(z - h) + ' '
        print(number)
dNumber(5)

''' Soal sekaligus jawaban '''

'''
#1              #3              #5

1               1               5
1 2             2 2             5 4
1 2 3           3 3 3           5 4 3
1 2 3 4         4 4 4 4         5 4 3 2
1 2 3 4 5       5 5 5 5 5       5 4 3 2 1

#2              #4              #6

1 2 3 4 5       1 1 1 1 1       5 4 3 2 1
1 2 3 4         2 2 2 2         5 4 3 2
1 2 3           3 3 3           5 4 3
1 2             4 4             5 4
1               5               5
'''