n = 0
m = 3
c = 3


pin = input("Buat PIN anda (XXYYY (XX = 2 digit NIM awal, YYY = 3 digit NIM akhir)) :")


while not (pin.isdigit() and len(pin)  == 5):
    pin = input("PIN harus 5 digit angka, buat kembali PIN anda : ")

while n < m :
    pin1 = input("Masukkan PIN anda :")
    
    if not (pin1.isdigit() and len(pin1) == 5):
        print("PIN harus 5 digit angka")
        continue
    if pin1 == pin :
        print("PIN benar, akses diterima")
        break
    else :
        n += 1
        c -= 1
        if n < m :
            print("PIN salah, sisa percobaan", c)
        else:
            print("Akses ditolak, kartu diblokir")