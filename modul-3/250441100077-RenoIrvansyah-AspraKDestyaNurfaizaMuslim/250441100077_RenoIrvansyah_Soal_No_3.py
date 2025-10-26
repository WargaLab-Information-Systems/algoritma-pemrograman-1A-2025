kalimat = input("Masukkan sebuah kalimat: ").lower()
hitung_vokal = 0
hitung_konsonan = 0
hitung_kata = 0

for i in kalimat:
    if i in ['a', 'i', 'u', 'e', 'o']:
        hitung_vokal += 1
print("Jumlah huruf vokal : ", hitung_vokal)

for j in kalimat:
    if j in ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]:
        hitung_konsonan += 1
print("Jumlah huruf konsonan : ", hitung_konsonan)

print("Jumlah huruf : ", hitung_konsonan + hitung_vokal)

for kata in kalimat.split():
    hitung_kata += 1
print("Jumlah kata : ", hitung_kata)