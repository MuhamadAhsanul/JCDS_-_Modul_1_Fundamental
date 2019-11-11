'''
Job Connector Data Science
Purwadhika Startup & Coding School
Selasa, 5 November 2019

C A T A T A N
'''

## CLASS & OBJECT ##


# Class

class kendaraan: 
    warna: 'merah'
    tahun: 2010

class MobilCustom():
    def __init__(self, warna, tahun, model):
        self.color = warna
        self.year = tahun
        self.model = model
    # method
    def jadul(self):
        if self.year < 2010:
            return True
        else : return False
    #check
    def tes(self):
        print(self.color, self.year, self.model, self.jadul())

mobil1 = MobilCustom('pink', 2019, 'x')
mobil2 = MobilCustom('blue', 2010, ['A', 'B'])
print(mobil1.color)
print(mobil2.year)
print(mobil1.model)
print(mobil2.model)

mobil1 = MobilCustom('merah', 1998, 'X')
mobil2 = MobilCustom('hijau', 2018, 'Z')
print(mobil1.year)
print(mobil1.jadul())
print(mobil1.tes())


# Inheritance

class Mobil:
    def __init__(self, warna, seat):
        self.warna = warna
        self.seat = seat
class Car(Mobil): # inheritance
    pass #retweet, mengulang operasi tanpa menulis kembali
    gps = True 
mobil1 = Mobil('Pink', 4)
car1 = Car('black', 8)
print(mobil1.warna, mobil1.seat)
print(car1.warna, car1.seat)
print(car1.warna, car1.seat, car1.gps)


# Def init

class X:
    def __init__(self, nama, gelar):
        self.nama = nama
        self.gelar = gelar        
class Y(X):
    def __init__(self, nama, gelar):
        X.__init__(self, nama, gelar)
class Z(X):
    pass
class A(X):
    def __init__(self, nama, gelar):
        super().__init__(nama, gelar)
        self.kampus = 'UGM'
objX = X('Andi', 'Prof')
objY = Y('Susi', 'dr')
print(objX.nama)

# -----------------------------------------

# Vars

class M:
    def __init__(self, nama, gelar):
        self.nama = nama
        self.gelar = gelar
class L(M):
    def __init__(self, nama, gelar, univ):
        super().__init__(nama, gelar)
        self.kampus = univ
objM = M('Andi', 'Prof')
objL = L('Susi', 'Dr.', 'UGM')
print(objL.nama, objL.gelar, objL.kampus)

from pprint import pprint
pprint(vars(objL))

print(vars(objM))
print(vars(objL))

# -----------------------------------

class H:
    nama = 'H'
    usia = 21
objH = H()
print(objH.nama)
print(objH.usia)

del H.nama
print(objH.usia)

class student:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia

# ------------------------------------

# Get Attribute & Has Attribute

class F:
    def __init__(self, nama, gelar):
        self.nama = nama
        self.gelar = gelar  
class G(F):
    def __init__(self, nama, gelar, univ):
        super().__init__(nama, gelar)
        self.kampus = univ
objF = F('Andi', 'Prof')
objG = G('Susi', 'Dr.', 'UGM')
print(objG.nama, objG.gelar, objG.kampus)

from pprint import pprint
pprint(vars(objG))

print(vars(objF))
print(vars(objG))
print(vars(objG))

print(objF.nama)
print(getattr(objG, 'gelar'))

# getattr = get attribute
# hasattr = has attribute

print(hasattr(objY, 'warna'))
print(hasattr(objY, 'Usia'))

# ------------------------------------------

# Set Attribute

objG.warna = 'Merah'
objH.usia = 23
setattr(objH, 'alamat', 'BSD')
print(vars(objH))

# -----------------------------------------

class N: 
    nama = 'N'
    usia = 21

objN = N()
print(objN.nama)
print(objN.usia)

del N.nama
print(objN.usia)

# -----------------------------------------