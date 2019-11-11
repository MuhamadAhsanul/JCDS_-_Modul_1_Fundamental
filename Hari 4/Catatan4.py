'''
Job Connector Data Science
Purwadhika Startup & Coding School
Kamis, 24 Oktober 2019

C A T A T A N
'''

### TUPLE & SET ###

''' Tuple () '''

x = [
    (1, [
        'a', 'b', 'c'
    ], 3),
    (4, 5, 6)
]

# list dalam tuple dapat diubah tapi tidak bisa sebaliknya
x[0][1][2] = 'Andi'
print(x)
x[0][1].append('d')
print(x)
x = tuple(x)
print(x)

x = [
    (1, ['a','b','c'], 3),
    (4, 5, 6)
]
x[0][1][2] = 'Andi'
x = tuple(x)
print(x)

x = [
    (1, ['a','b','c'], 3),
    (4, 5, 6)
]
x[0][1][2] = 'Andi'
x[0][1].append('d')

x = tuple(x)
x [0][1][2] = 'Budi'
print(x)

a = [1,2,3]
b = (1,2,3)
print(b[0])
print(type(b))

# tuple = immutable

'''
set/himpunan {}
1. no indexing
2. duplicate elements were not allowed
3. set mutable, but elements were immutable
'''

x = [1,2,3,1,2,3]
y = (1,2,3,1,2,3)
z = {1,2,3,1,2,3}
print(z)
print(set(list(x)))
z.add('a')
z.add(('c','d','e'))
print(z)

x = [1,2,3,1,2,3]
y = (1,2,3,1,2,3)
z = {1,2,3,1,2,3}

# mengubah set menjadi list
z = list(z)
print(z)
print(z[0])

# mengubah set menjadi list melalui loop
z = {1,2,3,1,2,3}
a = []
for i in z:
    a.append(i)
print(a)
z = {1,2,3,1,2,3}
z.add('a')
z.add(('b', 'c', 'd'))
print(z)

# Perbedaan 'add' dan 'update'
# Untuk 'add' dia menambahkan satu kesatuan          ('Andi') = ('Andi') ke dalam 'set' {}
# Untuk 'update' dia menambahkan menjadi per-elemen  ('Andi') = ('A', 'n', 'd', 'i') ke dalam 'set' {}
# Pada 'add' tipe data tidak di abaikan, contoh   ([1, 2, 3]) = {[1, 2, 3]}
# Pada 'update' tipe data di abaikan,    contoh   ([1, 2, 3]) = {1, 2, 3}


z.update('Andi')
print(z)
z.update([6,7,8])
print(z)
z.update({'z','budi'})
print(z)
print('budi' in z)

#  menghapus elemen menggunakan .remove dan .discard
z.remove('budi')
print(z)
z.discard('z')
print(z)

# menghapus elemen pertama dan seterusnya menggunakan .pop
z.pop()
z.pop()
print(z)

#  menghapus satu baris dengan .clear 
z.clear()
print(z)

# menghapus dengan _delete
del z
print(z)


''' SET {} '''

a = list('abcde')
b = list('bcfgh')
print(a)
print(b)
a = set (a)
b = set (b)

# irisan dari himpunan / intersection
print(a.intersection(b))
print(b.intersection(a))
print(a & b)
print(b & a)

# gabungan dari himpunan / union
print(a.union(b))
print(b.union(a))
print(a | b)
print(b | a)

# selisih dari himpunan / difference
print(a.difference(b))
print(b.difference(a))
print(a - b)
print(b - a)

# beda setangkup / symmetric difference
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))
print(a ^ b)
print(b ^ a)

# frozenset = set imutable
x = set([1,2,3])
y = frozenset([1,2,3])
x.remove(2)
# y.remove(2) tidak bisa di remove
print(x)
print(y)
print(x)
print(y)

P = {1,2,4,7,9,19}
Q = {7,6,9,19,5,12,16,17}
R = {3,8,6,19}

print(P.intersection(Q))
print(Q.intersection(P)) 
print(P.intersection(Q.intersection(R)))
print(P & (Q & R))