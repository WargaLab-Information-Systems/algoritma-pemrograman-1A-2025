# Modul 2

#Program Perintah if
# nama = "phyton"
# if nama == "phyton":
#     print("Hallo " + nama)

#Program Perintah if..else
# Kunci = "Python"
# password = input("Masukkan Password : ")
# if password == Kunci:
#     print("Password Benar")
# else:
#     print("Password Salah") 

# #Program Perintah if..elif..else
# angka = int(input("Masukkan sebuah bilangan : "))
# if angka > 0:
#     print("Angka merupakan Bilangan Positif")
# elif angka < 0:
#     print("Angka merupakan Bilangan Negatif")
# else:
#     print("Angka merupakan 0")

#Program If Bersarang
# x = int(input("Masukkan Nilai x="))
# y = int(input("Masukkan Nilai y="))
# if x == y:
#     print("nilai", x, "dan", y, "mempunyai nilai yang sama")
# else:
#     if x > y:
#         print(x, "lebih besar dari", y)
#     else:
#         print(x, "lebih kecil dari", y)

# Kendaraan = input("Masukkan Jenis Kendaraan (mobil pribadi, truk kecil, truk besar): ")
# Pembayaran = input("Masukkan Jenis Pembayaran (e-money, tunai): ") 
# Jam = int(input("Masukkan Jam Kedatangan (0-23): ")) 
# if Kendaraan == "mobil pribadi":
#     tarif = 15.000
# elif Kendaraan == "truk kecil":
#     tarif = 25.000
# elif Kendaraan == "truk besar":
#     tarif = 40.000
# else:
#     print("Jenis Kendaraan Tidak Dikenal")
# if Pembayaran == "e-money":
#     if Jam >= 23 or Jam <= 5:
#         diskon = 0.20 * tarif
#         print("Tarif: ", tarif - diskon)
#     else:
#         diskon = 0.10 * tarif
#         print("Tarif: ", tarif - diskon)
# elif Pembayaran == "tunai":  
#     diskon = 0
#     print("Tarif: ", tarif - diskon)
# else:
#     print("Pembayaran tidak valid")

# ======= IF =======
# x = 4
# if x == 5:
#     print("x sama dengan 5")

# x = "alproA"
    
# if x == "alproA":
#     print("saya sedang di kelas" + x)

# ======= IF ELSE =======
# password = "alproa"
# if password == "alprob":
#     print("password sesuai")
# else:
#     print("password tidak valid")

# nilai = 4
# if nilai == 4:
#     print("nilai tersebut 4")
# else:
#     print("nilai tidak 4")

# ======= IF ELIF ELSE =======
# nilai = int(input("Masukkan nilai anda:"))
# if nilai >= 80 <= 100:
#     print("Nilai anda bagus")
# elif nilai >= 70 < 79:
#     print("Nilai anda lumayan bagus")
# else:
#     print("Nilai anda jelek")

nilai = int(input("Masukkan nilai anda:"))
if nilai >= 80 and nilai <= 100:
    print("Nilai anda bagus")
elif nilai >= 70 or nilai < 79:
    print("Nilai anda lumayan bagus")
else:
    print("Nilai anda jelek")

# x = 10
# if x >= 5:
#     print("x lebih besar dari 5")

# if x <= 10:
#     print("x lebih kecil dari 15")

#======= IF BERSARANG =======
# x = int(input("Masukkan nilai x: "))
# y = int(input("Masukkan nilai y: "))

# if x == y:
#     print("Nilai x sama dengan y")
# else:
#     if x > y:
#         print("Nilai x lebih besar dari y")
#     elif x < y:
#         print("Nilai x lebih kecil dari y")
#     elif x == 0:
#         print("Nilai x adalah 0")

# ======= IF TERNARY =======
# nilai = int(input("Masukkan nilai: "))
# print("Lulus") if nilai >= 75 else print("Coba lagi")

# PERCOBAAN 1

# x = int(input("Masukkan bilangan: "))
# if x % 2 == 0:
#     print("Bilangan genap")
# else:
#     print("Bilangan ganjil")