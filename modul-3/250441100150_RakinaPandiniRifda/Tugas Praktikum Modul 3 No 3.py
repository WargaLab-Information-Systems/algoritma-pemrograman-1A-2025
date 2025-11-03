# Meminta input kalimat dari pengguna
kalimat = input("Masukkan sebuah kalimat: ")

# Mendefinisikan variabel
vokal = "aiueoAIUEO"
jumlah_vokal = 0
jumlah_konsonan = 0

# Menghitung jumlah huruf vokal dan konsonan
for huruf in kalimat:
    if ('A' <= huruf <= 'Z') or ('a' <= huruf <= 'z'): # Huruf alfabet
        if huruf in vokal:
            jumlah_vokal += 1
        else:
            jumlah_konsonan += 1

# Menghitung jumlah kata
jumlah_kata = 0
dalam_kata = False

for karakter in kalimat:
    if karakter != " ":  # mengecek spasi
        if not dalam_kata:
            jumlah_kata += 1
            dalam_kata = True
    else:
        dalam_kata = False

print("======== Hasi Analisis ========")
print(f"Jumlah huruf vokal     : {jumlah_vokal}")
print(f"Jumlah huruf konsonan  : {jumlah_konsonan}")
print(f"Jumlah kata            : {jumlah_kata}")