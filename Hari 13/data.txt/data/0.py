# import csv
# with open('data.csv', 'r') as x:
#     baca = csv.reader(x)
#     print(list(baca)

x = ['no', 'nama']
y = [12, 'Andi']
print(dict(zip(x,y)))

import csv
with open('data.csv', 'r') as x:
    baca = csv.DictReader(x)
    for i in baca:
        print(dict(i))

data = [
    {'nama':'Andi', 'usia':22, 'kota':'Jakarta'},
    {'nama':'Budi', 'usia':23, 'kota':'Bandung'},
    {'nama':'Caca', 'usia':24, 'kota':'Jakarta'}
]

with open('data.csv', 'w', newline='') as y:
    kolom = ['nama','usia','kota']
    a = csv.DictWriter(y, fieldnames=kolom)
    a.writeheader()
    a.writerows(data)

import json
with open('file.json', 'r') as x:
    out = json.load(x)
with open('haha.json', 'w') as y:
    json.dump(out, y)