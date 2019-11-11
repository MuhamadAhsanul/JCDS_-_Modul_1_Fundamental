'''
Job Connector Data Science
Purwadhika Startup & Coding School
Rabu, 30 Oktober 2019

T U G A S
'''

def ubahVokal(kata):
    output = ''
    for huruf in kata.lower():
        if huruf in 'aiueo':
            output = output + 'o'
        else:
            output = output + huruf
    return output

x = input('Masukkan kata : ')
print(ubahVokal(x))

x = 'malama'
y = list(x[::-1])   # Sebenarnya tanpa list, dapat di putar balik 'Kata' nya
y = ''.join(y)      # Dapat mengubah list menjadi string kembali

def palindrome(kata):
    if kata == y:
        return True
    else:
        return False

print(palindrome(x))


'''
kalimat = 'Hai Aku Lintang' #dibalik
# ==================================
mengubah morse menggunakan aplikasi dalam python
Lintang ?
# ==================================
Caesar Cipher, soalnya : positif
'''

## KALIMAT DIBALIK ##
kalimat = 'Hai Aku Lintang'
kalimat = kalimat.split()
print(kalimat)

kalimat = input('Masukkan kalimat : ')
kalimat = kalimat.split()

def balikPosisi(myList):
    z = ''
    for y in myList:
        x = y[::-1] + ' '
        z += x
    return z

print(balikPosisi(kalimat))

## CAESAR CIPHER ##

x = input('Masukkan random kata : ')
y = int(input('Masukkan jumlah yg di geser : '))
def caesarChipher(kata):
    hasil = ''
    for huruf in kata.lower():
        if huruf in alfabet:
            indexHuruf = alfabet.index(huruf)
            indexHuruf = indexHuruf + (y%26)
            if indexHuruf >= 26:
                indexHuruf -= 26
                hasil = hasil + alfabet[indexHuruf]
            else:
                hasil = hasil + alfabet[indexHuruf]
        else:
            hasil = hasil + huruf
    return hasil

print(caesarChipher(x))

## MORSE ##

kamus = {
    'A':'._', 'B':'_...', 'C':'_._.', 'D':'_..', 'E':'.', 
    'F':'.._.', 'G':'__.', 'H':'....', 'I':'..', 'J':'.___',
    'K':'_._', 'L':'._..', 'M':'__', 'N':'_.', 'O':'___',
    'P':'.__.', 'Q':'__._', 'R':'._.', 'S':'...', 'T':'_',
    'U':'.._', 'V':'..._', 'W':'.__', 'X':'_.._', 'Y':'_.__', 'Z':'__..', 
    '1':'.____', '2':'..___', '3':'...__', '4':'...._', '5':'.....',
    '6':'_....', '7':'__...', '8':'___..', '9':'____.', '0':'_____'
}

alfabet = list(kamus)
morse   = list(kamus.values())

kata = input('Masukkan kata/kalimat : ')

def sandiMorse(word):
    output = ''
    word = word.upper()
    word = word.split()
    # word = ''.join(word)
    for i in word:
        if i in alfabet:
            morse_1 = morse[alfabet.index(i)]
            output = output + morse_1 + ' / '
        elif i in morse:
            alfabet_1 = alfabet[morse.index(i)]
            output = output + alfabet_1
        elif i == '/':
            output = output + ' '
        else:
            output = output + i + ' / '
    return output

print(sandiMorse(kata))