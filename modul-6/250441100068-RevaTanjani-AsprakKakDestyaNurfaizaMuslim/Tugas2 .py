def gabung_tuple(t1, t2):
    gabung = t1 + t2
    
    a = []
    for x in gabung:
        if x not in a:
            a.append(x)

    hasil = []
    while a:
        maks = a[0]
        for x in a:
            if x > maks:
                maks = x
        hasil.append(maks)
        
        a.remove(maks)

    return tuple(hasil)

try:
    t1 = tuple(map(int, input("Tuple 1 (pisah koma): ").split(",")))
    t2 = tuple(map(int, input("Tuple 2 (pisah koma): ").split(",")))
    print(gabung_tuple(t1, t2))
except:
    print("Input salah, hanya angka dipisah koma.")
