t1 = ()
for i in range(int(input("masukkan jumlah tuple pertama : "))):
    t1 += (int(input("angka tuple pertama : ")),)

t2 = ()
for i in range(int(input("masukkan jumlah tuple kedua : "))):
    t2 += (int(input("angka tuple kedua : ")),)

a = ()
for x in t1 + t2:
    if x not in a:
        a += (x,)

b = ()
for x in a:
    b += (x,)

hasil = ()
while b:
    maks = b[0]
    for x in b:
        if x > maks:
            maks = x

    hasil += (maks,)

    baru = ()
    sudah = False
    for x in b:
        if x == maks and not sudah:
            sudah = True
            continue
        baru += (x,)
    b = baru
print("hasilnya adalah :", hasil)
