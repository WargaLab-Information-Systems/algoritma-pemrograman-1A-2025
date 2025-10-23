# #simulasi sederhana mesin atm
# #memasukkan PIN( X = 2 nim awal, y = 3 nim terakhir)
# # Pin benar akses diterima, Pin salah coba lagi
# # Pin berbentuk angka 5 digit dan kesempatan mencoba 3 kali
# # tiga kali salah kartu di blokir

# PIN_BENAR = 25122
# kesempatan = 3

# while kesempatan > 0:
#     pin = input("Masukkan PIN 5 digit Anda: ")

#     # Pastikan semua karakter angka dengan cara manual
#     angka = True
#     for karakter in pin:
#         if karakter < '0' or karakter > '9':   # cek satu per satu
#             angka = False
#             break

#     if angka:
#         pin = int(pin)
#         if pin >= 10000 and pin <= 99999:   # cek 5 digit
#             if pin == PIN_BENAR:
#                 print("PIN benar, akses diterima")
#                 break
#             else:
#                 kesempatan -= 1
#                 if kesempatan > 0:
#                     print("PIN salah, coba lagi. Kesempatan:", kesempatan)
#                 else:
#                     print("Akses ditolak, kartu diblokir")
#         else:
#             kesempatan -= 1
#             if kesempatan > 0:
#                 print("PIN harus 5 digit angka, kesempatan:", kesempatan)
#             else:
#                 print("akses ditolak, kartu di blokir")
#     else:
#         kesempatan -= 1
#         if kesempatan > 0:
#             print("PIN harus berupa angka, kesempatan", kesempatan)
#         else:
#             print("akses ditolak, kartu di blokir")
angka = 10
for i in range(5,10 + 5):
    print(i)