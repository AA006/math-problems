
# 1+n+n²+n³+n⁴+n⁵=i² ifadesini sağlayan i tam sayısı kaçtır?



import math
def us(x, y):
    t = int(math.pow(x, y))
    return t


def kontrol(i):
    a = us(i, 1) + us(i, 2) + us(i, 3) + us(i, 4) + us(i, 0)
    for j in range(0, a):
        if j == math.sqrt(a):
            print(i, " ", a, " ", j)


for i in range(0, 10):
    print(i)
    kontrol(i)
