t1 = ()
t2 = ()
banyak1 = int(input("masukan banyak nilai pada tuple ke - 1 "))
for i in range(banyak1):
    nilai1 = int(input("masukan nilai "))
    t1 = t1 + (nilai1,)

banyak2 = int(input("masukan banyak nilai pada tuple ke - 2 "))
for i in range(banyak2):
    nilai2 = int(input("masukan nilai "))
    t2 = t2 + (nilai2,)

gabung = t1 + t2
print(f"tuple ke - 1 {t1}")
print(f"tuple ke - 2 {t2}")
print(f"setelah di gabung {gabung}")

beda = []
for i in gabung:
    if i not in beda:
        beda.append(i)

print(f"setelah elemen duplikat di hapus {beda}")

n = len(beda)
for i in range(n - 1):
    mak = i
    for k in range(i + 1, n):
        if beda[k] > beda[mak]:
            mak = k
    beda[i], beda[mak] = beda[mak],beda[i]

print(f"setelah di urutkan {beda}")