'''
Job Connector Data Science
Purwadhika Startup & Coding School
Senin, 21 Oktober 2019

C A T A T A N
'''

print(12+2)
print('budi' + 'andi')
print('budi' + '12')

# Variables
nama = "Andi" #string (kata)
usia = 12     #integer (angka)
tinggi = 189.3 #float (koma)
jomblo = False #boolean
# print(type(class)) untuk mengetahui class dari variabel dalam kurung. 
#                    apakah float, string, integer, atau boolean'''
print(type(nama))
print(type(usia))
print(type('1234'))
print(type(tinggi))
print(type(jomblo))
print('halo, aku ' + nama)
print(type(float(usia)))
print('Umurku', usia)
print('umurku ' + str(usia)) # str berfungsi untuk mengubah data dari class asal menjadi string'''

# string
nama = 'Kocheng' #string 

# lower atau upper untuk mengetahui besar kecil karakter
print(nama.lower())
print(nama.upper())
x = 'hahahaha'

# is diberikan di depan upper atau lower berfungsi untuk menanyakan
print(x.islower())
print(x.isupper())
print(nama.lower().isupper())
print(nama.upper().isupper())

# len = length atau panjang
print(len(nama) + 4)
print(len(nama))

# print(nama[0 / 1 / 2 / 3 / dst]) 
'''berfungsi untuk mengetahui huruf tertentu yang disebutkan dalam angka'''
print(nama[0])

# [start : stop : step]
'''berfungsi untuk mencari kata berdasarkan angka dimulai dan angka berakhir'''
print(nama[3 : len(nama) : 2])
print(nama[-3])

nama = 'Purwadhika Startup & Coding School'
print('Purwadhika Statup & Coding School')
print(nama[0])
print(nama[-3])
print(nama.lower().count('startup'))
print(nama.lower().count('a'))
print(nama.upper())
print(nama.lower())
print(nama[3 : len(nama) : 1])
print(len(nama))
print(len(nama) + 6)

nama = 'Andi'
print(nama)
usia = 22
print(usia)
jomblo = False
print(jomblo)
print(type(nama))
print(type(usia))
print(type(jomblo))

nama = input("whats your name? : ")
print(nama)
usia = input("how old are you? : ")
print(usia)
alamat = input("give me your address please? : ")
print(alamat)
pekerjaan = input("kowe kerjo po nganggur? : ")
# print(pekerjaan)

# Numbers & Arithmetic Operators
ANDI = 40
BUDI = 55

print(ANDI * BUDI)
print(ANDI - BUDI)
print(ANDI / BUDI)
print(ANDI + BUDI)
print(ANDI ** 2)
print(BUDI ** 2)

print(ANDI + 3)
print(BUDI * 4)
