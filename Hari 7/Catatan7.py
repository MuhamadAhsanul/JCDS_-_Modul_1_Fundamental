'''
Job Connector Data Science
Purwadhika Startup & Coding School
Rabu, 30 Oktober 2019

C A T A T A N
'''
## FIZZBUZZ, REVERSE, PALINDROME,  ##

for i in range(1,11):
    if 1 % 2 == 0:
        print('WOW!')
    else:
        print(i)

def fizzbuzz(num) :
    for i in range(1,num+1):
        if (i % 15 == 0):
            print('FizzBuzz')
        elif (i % 3 == 0):
            print('Fizz')
        elif (i % 5 == 0):
            print('Buzz')
        else : 
            print(i)

fizzbuzz(300)

# x = [1,2,3,4,5,6,7]
# y =['Andi', 'Budi', 'Caca']

import math

# 1 reverse
# x.reverse()
# print(x)

# 2 reverse
# print(x[::-1])

# 3 reversed()
# print(list(reversed(x)))

def reverseList(theList) :
    for i in range(0, math.floor(len(theList)/2)) :
        tempList = theList[i]
        theList[i] = theList[len(theList) - 1 - i]
        theList[len(theList) - 1 - i] = tempList
    
    return theList
print(reverseList([1,2,3,4,5,6,7]))

x = [1,2,3,4,5,6,7]
y = ['Budi', 'andi', 'caca']

def balikPosisi(mylist):
    hasil = []
    for i in range(len(mylist)):
        hasil.insert(0, mylist[i])
    return hasil

print(balikPosisi(x))
print(balikPosisi(y))

# lintang => lontong
vocalWords = list('aiueo')
print(vocalWords)

def changevocal(param): 
    newString = ''
    for i in param:
        if i in vocalWords:
            i = 'o'
            newString += i
        else:
            newString += i

    print(newString)

# changevocal(input('masukkan kata:').lower())

'''PALINDROME'''

my_str = 'katak'
my_str = my_str.casefold()
rev_str = reversed(my_str)
if list(my_str) == list(rev_str):
    print("True")
else:
    print("False")

#atau

x = 'malam'

def palindrome(kata):
    if kata == kata[::-1]:
        return True
    else:
        return False
print(palindrome(x))

# atau 

def palindrome2(kata):
    for i in range(round(len(kata)/2)):
        palindromekah = False
        if kata[i] == kata[len(kata)-1-i]:
            palindromekah = True
        else:
            palindromekah = False
            break
    return palindromekah
print(palindrome2('katak'))
print(palindrome2('oppok'))

