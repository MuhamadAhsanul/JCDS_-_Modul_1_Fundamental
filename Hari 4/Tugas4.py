'''
Job Connector Data Science
Purwadhika Startup & Coding School
Kamims, 24 Oktober 2019

T U G A S

'''

## SOAL ##

# S = {bilangan cacah > 11}
# A = {x|x<10, bilangan prima}
# B = {5, 7, 9}

S = []
A = []
B = []

for i in [0, 11, 1]:
    S.append(i)

for i in [2, 3, 5, 7]:
    A.append(i)

for i in [5, 7, 9]:
    B.append(i)

S = set(S)
A = set(A)
B = set(B)

op_1 = (A & B)
op_2 = (A | B)
op_3 = (A & op_2)
op_4 = (B & op_2)
op_5 = (op_2 & op_2)
op_6 = (op_1 & op_2)

print(f'Irisan dari A dan B adalah {op_1}')
print(f'Gabungan dari A dan B adalah {op_2}')
print(f'Operasi A ∩ (A ∪ B) adalah {op_3}')
print(f'Operasi B ∩ (A ∪ B) adalah {op_4}')
print(f'Operasi (A ∪ B) ∩ (A ∪ B) adalah {op_5}')
print(f'Operasi (A ∩ B) ∪ (A ∪ B) adalah {op_6}')



