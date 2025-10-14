# soal no 3 09okt2025

kalimat = input("Masukkan kalimat: ")
vokal = 0
konsonan = 0
kata = 1
vokal = "AIUEO"
for i in kalimat.upper():
    if i in vokal:
        vokal += 1
    elif i in "bcdfghjklmnopqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
        konsonan += 1
    elif i == " ":
        kata += 1

print("Jumlah huruf vokal: ", vokal)
print("Jumlah huruf konsonan: ", konsonan)
print("Jumlah kata: ", kata)

