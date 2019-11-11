'''
Job Connector Data Science
Purwadhika Startup & Coding School
Jumat, 1 November 2019

C A T A T A N
'''

## LOOPING USING STAR TRIANGLE ##


# Inverted Triangle

def rStar(x):
    star = ''
    for i in range (x):
        star = '*' * (x - i)
        print(star)

rStar(8)

# Normal, But Using Numbers

n = int(input("enter the number of rows:"))
for i in range (1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

# Inverted Right Triangle of Numbers

rows = int(input("enter the numbers of rows:"))

print("Inverted Right Triangle Pattern of Numbers:") 
i = rows
while(i >= 1):
    for j in range(1, i + 1):      
        print('%d ' %i, end = '  ')
    i = i - 1
    print()

# Floyd's Triangle

rows = int(input("Please Enter the total Number of Rows  : "))
number = 1

print("Floyd's Triangle") 
for i in range(1, rows + 1):
    for j in range(1, i + 1):        
        print(number, end = '  ')
        number = number + 1
    print()

# REKURSIF FUNGSI #

def pangkat(x, y):
    pangkat = 1
    for pangkat in range(y):
        pangkat *= x
    print(f'Jawaban dari {x} pangkat {y} adalah {pangkat}')
pangkat(2, 3)

# Function yang memanggil dirinya sendiri dinamakan "Rekursif Fungsi"
def pangkatB(x, y):
    if (y == 1):
        return x
    else:
        return x * pangkatB(x, y-1)
print(pangkatB(2,3))