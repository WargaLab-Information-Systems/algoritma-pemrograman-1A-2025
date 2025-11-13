# SOAL 1
X = str("SOAL 1")
print(X)

def faktorial (i):
    if i == 0  or i == 1:
        return 1
    else:
        return i * faktorial (i-1)
    
k = int(input("Silahkan masukkan angka N: "))
if k < 0:
    print("maaf angka tidak valid")
else:
    hasil = faktorial (k)
    print (f"Faktorial dari {k} adalah {hasil}")