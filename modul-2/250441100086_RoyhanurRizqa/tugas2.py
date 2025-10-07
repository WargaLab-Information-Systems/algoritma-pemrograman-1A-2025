usia=int(input("masukkan usia anda : "))
hari=str(input("masukkan hari :")).lower()
status_p=str(input("apakah anda pelajar SMA(ya/tidak) :")).lower()
status=str(input("memiliki kartu pelajar (ya/tidak) :")).lower()

tiket=50000
if usia < 12:
    diskon = 0.5
elif status == "ya" and status_p == "ya":
    diskon = 0.3
elif hari == "selasa":
    diskon = 0.2
else:
    diskon = 0

harga_akhir=tiket-(tiket*diskon)
print("Harga tiket normal : Rp", tiket)
print("Diskon             :", diskon*100, "%")
print("Harga yang harus dibayar : Rp", int(harga_akhir))