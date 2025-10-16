kalimat = input("Masukkan kalimat: ")

vokal = "aiueoAIUEO"
jumlah_vokal = 0
jumlah_konsonan = 0

for huruf in kalimat:
    if huruf.isalpha():
        if huruf in vokal:
            jumlah_vokal += 1
        else:
            jumlah_konsonan += 1

kata = kalimat.split()
jumlah_kata = len(kata)

print(f"Jumlah huruf vokal: {jumlah_vokal}")
print(f"Jumlah huruf konsonan: {jumlah_konsonan}")
print(f"Jumlah kata: {jumlah_kata}")                        