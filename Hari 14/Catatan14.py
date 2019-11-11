# Fibonacci
# 0,1,1,2,3,5,8,13,21,34,55,89,144

class fibo:
    def fibo1(self, x):
        a = range(101)
        ac = []
        for i in a:
            if i <= 1:
                ac.append(1)
            else:
                rumus = ac[i - 1]+ac[i - 2]
                ac.append(rumus)
        Fi = ac[x]
        return Fi

Objek = fibo()
print(Objek.fibo1(2))
print(Objek.fibo1(40))