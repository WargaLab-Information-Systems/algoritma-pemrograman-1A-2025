print("="*15," Tugas 3 Program Analisis Kalimat ","="*15)

# Inputan Pengguna 
k = input("Masukkan Sebuah Kalimat : ").lower()

#variabel Pandangan 
vokal = "aiueo"
jv = 0
jko = 0 

#menghitung Jumlah Huruf Vokal, konsonan
for huruf in k:
    if huruf.isalpha(): # Untuk Mengecek Tipe Data String Kalau Tidak String Maka Tidak Di hitung
        if huruf in vokal:
            jv += 1
        else:
            jko += 1 

# menghitung Jumlah kata 
jka = len(k.split()) #tools Yang digunakan Untuk Memecah String

#outputan 
print("\n=== Hasil Analisis Dari Kalimat Di Atas Adalah : ===")
print(f"Jmlah Dari Huruf Vokal     : {jv}")
print(f"Jumlah Dari Huruf Konsonan : {jko}")
print(f"Jumlah Kata                : {jka}")