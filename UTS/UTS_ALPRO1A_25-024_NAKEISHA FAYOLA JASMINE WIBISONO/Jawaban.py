beras = 12000
gula = 14000
minyak = 20000
member_card = input("Apakah memiliki member card? ya/tidak: ").lower()
total = 0

while True:
    barang = str(input("Masukkan jenis barang: ")) 
    jumlah = int(input("Masukkan harga barang: "))
    
    diskon = 0
    if total > 100000:
        diskon = 10
    elif total > 200000:
        diskon = 15
    elif total > 150000 and total <= 200000:
        diskon = 10
    else:
        print("jumlah sama")
        break
    
    if member_card == "ya":
        diskon = 5
    else:
        break
    
    total_belanja = diskon * jumlah
    total_akhir = total_belanja * (diskon * 100)
    
print("jenis barang", barang)
print("jumlah barang", jumlah)
print("diskon: ", diskon)
print("Total belanja: ", total_belanja)
print("total akhir: ", total_akhir)
        
    
        
