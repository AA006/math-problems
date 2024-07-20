
# (n⁵-1)/2=i² ifadesini sağlayan i tam sayısı kaçtır?



import math

def us(x, y):
    t = int(math.pow(x, y))
    return t


def kontrol(i):
    z = int((us(i, 5)-1)/2)
    for k in range(1, z):
        if k == math.sqrt(z):
            print(i, k, z)


for i in range(1000):
    print(i)
    kontrol(i)
