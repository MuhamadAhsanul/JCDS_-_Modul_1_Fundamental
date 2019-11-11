'''
Job Connector Data Science
Purwadhika Startup & Coding School
Jumat, 25 Oktober 2019

T U G A S

'''

days = {
    'senin' : 'Monday', 'Seloso' : 'Tuesday', 'Rebo' : 'Wednesday', 'Kemis' : 'Thursday',
    'Jumuah' : 'Friday', 'Sebtu' : 'Saturday', 'Minggu' : 'Sunday'
}

# --- jawa = eng
input('sebutno jeneng dinone : ')
hari = input('sebutno jeneng dinone : ')
print(f'{hari.capitalize()} = {days.get(hari.capitalize(), "GA ADA CUK!")}')



# eng-jawa
days = {
    'monday' : 'senen', 'tuesday' : 'seloso', 'wednesday' : 'rebo',
    'thursday' : 'kemis', 'friday' : 'jemuah', 'saturday' : 'sebtu',
    'sunday' : 'minggu'
    }


hari = input('mensyen name of the deys : ')
print(f'{hari.upper()} = {days.get(hari.lower(), "Ngawur rak enek woi!")}')

days = {
    'senin' : 'Monday', 'Seloso' : 'Tuesday', 'Rebo' : 'Wednesday', 'Kemis' : 'Thursday',
    'Jumuah' : 'Friday', 'Sebtu' : 'Saturday', 'Minggu' : 'Sunday'
}

'''
hari = input('mensyen name of the deys : ')
print(list(days))
print(list(days.values()))
'''

hari = list(days)
day = list(days.values())

x = input('ketik nama hari (ENG/JOW) : ')
if x.lower() in hari:
    engHari = day[hari.index(x.lower())]
    print(f'Bhs Inggris{x.lower()} adalah {engHari}')
else : 
    jowDay = hari[day.index(x.lower())]
    print(f'Bhs Jowo{x.lower()} adalah {jowDay}')

nilai = 98

if nilai >= 82:
    print('Nilai anda A')
elif nilai in range(72, 81):    # atau (nilai >= 72) and (nilai <=81)
    print('Nilai anda B')
elif nilai in range(62, 71):    # atau (nilai >= 62) and (nilai <=71)
    print('Nilai anda C')
elif nilai in range(52, 61):    # atau (nilai >= 52) and (nilai <=61)
    print('Nilai anda D')
else:
    print('Nilai anda E')