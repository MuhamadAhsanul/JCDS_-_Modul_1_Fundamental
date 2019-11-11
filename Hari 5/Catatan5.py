'''
Job Connector Data Science
Purwadhika Startup & Coding School
Jumat, 25 Oktober 2019

C A T A T A N
'''

## DICTIONARY ##

andi = {
    'nama':'Andi',
    'age':22,
    'is_married':False,
    'job':'PNS',
    'cars':['Alphard','Rush','Innova'],
    'address':{
        'street':'Mawar Ungu',
        'RT':5,
        'RW':5,
        'Kecamatan':'Smallville',
        'zipcode':14045,
        'geo': {
            'lat':209.22,       # Latitude
            'lng':55.67         # Longitude
        }
    }
}

andi['nama'] = 'Budi'           # nama list [index]
andi['salary']=32000000
andi.update({'no_ktp':3215142304960002})

print(list(andi))
print(andi.keys())
print(list(andi.values())) # hanya valuesnya saja, bukan keysnya.
print(list(andi.keys())) # hanya keysnya saja, bukan valuenya. keys = pertanyaan, values = keterangan

print(andi)
print(andi['cars'][1])
print(andi['address']['Kecamatan'])
print(andi['nama']) # Andi
print(andi['age']) # 22
print(andi['is_married']) # False

# untuk menghindari error apabila keys tidak ada dalam data
print(andi.get('nama')) # Andi
print(andi.get('age')) # 22
print(andi.get('is_married')) # False
print(andi['job']) # PNS
print(type(andi)) # PNS

# untuk me-replace elemen di dalam data
andi['name'] = 'Budi'
print(andi)

print(andi['cars'])
print(andi['cars'][0])

# meng-extract informasi dari 'address'
print(andi['address']['geo'])

# Untuk mengetahui 'keys' di dalam dictionary
print(list(andi))
print(list(andi.keys()))

# Untuk mengetahui 'values' di dalam dictionary
print(list(andi.values()))

# Untuk menambahkan elemen
andi['salary'] = 25000000
andi.update({'no_ktp' : 234089})
print(andi)

# Untuk memperlihatkan semua konten yg ada di dalam 'set'
x = {1: True, 2: False}
print(list(x.items()))


# if statement
# if condition:
#     program():
# satu sama dengan (=) berarti assign values
# dua sama dengan (==) berarti sama dengan

# if, elif & else

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

x = 4

if x == 4:
    print('ini 4')
else : 
    print('ini bukan 4')


''' maka jawabannya : ini 4, menyesuaikan variabel
    namun jika variable nya beda seperti : ''' 

if x == 5:
    print('ini 4')
else : 
    print('ini bukan 4')

'''
maka jawabannya : ini bukan 4, lagi-lagi menyesuaikan
variabel. 
'''

#equation
x = '4'
print(x==4)
print(x>=4)
print(x<=4)

# comparison
x = '4'
print(x<4)
print(x>4)
print(x!=4)

# if statement
''' membandingkan kondisi antara satu 
    nilai dengan nilai yang lain '''

# nilai = 60 (wes remed ae kene)
# nilai = 90 (congratulation!)
nilai = 80
if nilai > 80:
    print('Congratulation!')
elif nilai < 40:
    print('Balio omah kowe')
else :
    print('wes remed ae kene')

# nilai = 60
# nilai = 20
if nilai > 80 :
    print(f'Weh nilaimu {nilai}, Muantep dek, auto surga kon')
elif nilai < 40 :
    print(f'Pakmu undangono, iki lho nilaimu sakmene {nilai}, Balio omah kowe')
# else :
#     print('wes remed ae kene')

jomblo = False; nganggur = False

if jomblo == True and nganggur == True:
    print('bukako linkedin dolanano tinder cuk')
elif  jomblo == True and nganggur == False:
    print('wibu!')
elif jomblo == False and nganggur == True:
    print('fix bucin asu')
else:
    print('yha')

# jawabannya : yha

jomblo = True; nganggur = False

if jomblo == True and nganggur == True:
    print('bukako linkedin dolanano tinder cuk')
elif  jomblo == True and nganggur == False:
    print('wibu!')
elif jomblo == False and nganggur == True:
    print('fix bucin asu')
else:
    print('yha')

# jawabannya : wibu!

jomblo = True; nganggur = True

if jomblo == True and nganggur == True:
    print('bukako linkedin dolanano tinder cuk')
elif  jomblo == True and nganggur == False:
    print('wibu!')
elif jomblo == False and nganggur == True:
    print('fix bucin asu')
else:
    print('yha')

# jawabannya : bukako linkedin dolanano tinder cuk

x = True; y = False
print(x and y) 
print(x or y)
x = 2; y = 5
print(x < 10 and y > 0)

nilai = 98

# nilai >= 82 : A 
# nilai 72 - 81 : B
# nilai 62 - 71 : C
# nilai 52 - 61 : D
# nilai <52 : E

if nilai >= 82 :
    print('A')
elif nilai >= 72 and nilai <= 81 :
    print('B')
elif nilai >= 62 and nilai <= 71 :
    print('C')
elif nilai >= 52 and nilai <= 61 :
    print('D')
elif nilai <= 52 : 
    print('E')