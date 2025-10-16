pin_benar = "25028"
kesempatan = 3
print("Masukkan PIN Anda (5 digit angka):")

for percobaan in range(1, kesempatan + 1):
    pin_input = input(f"Percobaan {percobaan}/{kesempatan}: ")
    
    if len(pin_input) != 5:
        print("PIN harus 5 digit angka! Coba lagi.")
        continue
    
    if pin_input == pin_benar:
        print("PIN benar, akses diterima")
        break
    else:
        print("PIN salah, coba lagi")
        
        if percobaan == kesempatan:
            print("Akses ditolak, kartu diblokir")