'''
Job Connector Data Science
Purwadhika Startup & Coding School
Selasa, 5 November 2019

T U G A S
'''

data = [
    {'nama' : 'Andi', 'usia' : '21'},
    {'nama' : 'Budi', 'usia' : '22'},
    {'nama' : 'Caca', 'usia' : '20'},
    {'nama' : 'Doni', 'usia' : '21'},
]

for i in data:
    stud = stud(i['nama'], i['usia'])
    print(f'{stud.nama} {stud.usia}')

def createObj(x):
    nama = x['nama']
    vars()[nama] = stud(x['nama'], x['usia'])
    return vars()[nama]
dataNew = list(map(createObj, data))
print(dataNew[0].nama)
print(dataNew[0].usia)

# atau
def createObj2(x):
    return stud(x['nama'], x['usia'])
dataNew = list(map(createObj2, data))
print(dataNew[1].nama)
print(dataNew[1].usia)

#atau
dataNew3 = list(map(
    lambda x: stud(x['nama'], x['usia']), data))
print(dataNew3[2].nama)
print(dataNew3[2].usia)

# -----------------------------------------------

'''
class keRomawi():
    ....

keRomawi(3) => III
keRomawi(5) => V
keRomawi(11) => XI
keRomawi(2019) => MMXIX
'''

romanDict = {
    'M' : 1000,
    'CM': 900,
    'D' : 500,
    'CD': 400,
    'C' : 100,
    'XC': 90,
    'L' : 50,
    'XL': 40,
    'X' : 10,
    'IX': 9,
    'V' : 5,
    'IV': 4,
    'I' : 1
}

def romanNum(param):
    newString = ''
    while param >= 1:
        for i in list(romanDict.values()):
            newString += (int(param/i) * list(romanDict.keys())[list(romanDict.values()).index(i)])
            param = param % i
    print(newString)

def numRom(param):
    angka = 0
    while param != romanDict:
        for i in len(param):
            x = param[i]
            y = param[i+1]
            a = romanDict.get(x)
            b = romanDict.get(y)
            if a >= b:
                angka += a
            elif x < y:
                z = b - a
                angka += z
    print(angka)

abc = list(input('Masukkan romawi : '))
numRom(abc)