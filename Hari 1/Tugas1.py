'''
Job Connector Data Science
Purwadhika Startup & Coding School
Senin, 21 Oktober 2019

T U G A S
'''

nama = 'Hari ini budi tidak masuk sekolah'
cari = 'h'
x = nama.lower().replace(cari.lower(), '')
print(x)

jmlCari = int((len(nama) - len(x)) / len(cari))
print(f'Jumlah kata \'{cari}\' ada = {jmlCari}')

nama2 = 'Hari ini Hari tidak masuk sekolah karena hari Minggu'
cari2 = 'hari'
x = nama2.lower().replace(cari2.upper(),'')
print(x)

jmlCari2 = int((len(nama2)-len(x))/len(cari2))
print(f'Jumlah kata \'{cari2}\' ada = {jmlCari2}')