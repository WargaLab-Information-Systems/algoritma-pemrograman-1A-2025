# variable
umur= int(input("masukkan umur: "))
status_pelajar= input("masukkan status pelajar (yes/no): ")
hari= input("masukkan hari apa: ")
Tiket=50000
# penyeleksian kondisi
if umur < 12:
     diskon = 0.50
elif status_pelajar == "yes":
        diskon = 0.30
elif hari == "selasa":
    diskon = 0.20
else:
    diskon = 0 
total = int(Tiket-Tiket*diskon)
hemat = Tiket-total
# print
print("===============================")
print("umur:", umur)
print("status pelajar: ", status_pelajar)
print("hari: ",hari)
print("===============================")
print("Diskon: ", (int(diskon*100)),"%")
print(f"Harga tiket: Rp {total}")
print(f"Hemat: Rp {hemat}")