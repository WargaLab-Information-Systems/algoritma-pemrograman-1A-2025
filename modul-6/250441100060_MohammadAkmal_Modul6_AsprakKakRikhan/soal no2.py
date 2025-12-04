# data tuple
t1 = (3,1,4)
t2 = (1,5,9)

gab = t1 + t2
hasil = []
for x in gab:
    if x not in hasil:
        hasil.append(x)

hasil.sort(reverse=True)

akhir = tuple(hasil)

print(akhir)
