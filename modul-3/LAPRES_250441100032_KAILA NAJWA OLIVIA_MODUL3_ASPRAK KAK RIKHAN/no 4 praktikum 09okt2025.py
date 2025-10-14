#soal no 4 09okt2025

while True:
    nama = input("Masukkan nama pelanggan: ")
    jumlah = int(input("Jumlah barang: "))  
    total = 0  
    print("Daftar barang:") 

    for i in range(jumlah):  
        barang = input("Nama barang: ")  
        harga = int(input("Harga: "))    
        total = total + harga 
# Tampilkan struk
    print("\n===== STRUK INDOMEI =====")
    print("Nama:", nama)
    print("Total:", total)
    print("Terima kasih berbelanja di IndoMei!")
    print("\n===== TERIMA KASIH =====")

    jawab = input("apakah ada pembeli berikutnya? (ya/tidak): ")
    if jawab == "tidak":
        break
