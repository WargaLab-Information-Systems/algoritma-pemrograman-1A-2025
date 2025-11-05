# # Meminta input kalimat dari user
# kalimat = input("Masukkan sebuah kalimat: ")

# # Daftar huruf vokal Dan Konsonan
# vokal = "aiueoAIUEO"
# huruf = "abcdefghijklmnopqrstuvwxyzABDCDEFGHIJKLMNOPQRSTUVWXYZ"

# # Inisialisasi penghitung
# jumlah_vokal = 0
# jumlah_konsonan = 
# jumlah_kata = 0

# # Variabel penanda apakah sedang berada di dalam kata
# dalam_kata = False

# for karakter in kalimat: # memeriksa karakter dr kalimat yang dimasukkan
#     # Hitung vokal dan konsonan
#     if karakter in huruf:
#         if karakter in vokal:
#             jumlah_vokal += 1
#         else:
#             jumlah_konsonan += 1

#         # Jika ketemu huruf dan sebelumnya bukan dalam kata, berarti awal kata baru
#         if not dalam_kata:
#             jumlah_kata += 1
#             dalam_kata = True
#     else:
#         # Jika karakter bukan huruf (misalnya spasi atau tanda baca), tandai keluar dari kata
#         dalam_kata = False

# # Tampilkan hasil
# print(f"Kalimat yang dimasukkan : {kalimat}")
# print(f"Jumlah huruf vokal      : {jumlah_vokal}")
# print(f"Jumlah huruf konsonan   : {jumlah_konsonan}")
# print(f"Jumlah kata             : {jumlah_kata}")

x = 3
y = 2
z = 4
hasil = x**y*z+x/y-y%z//x
print(hasil)