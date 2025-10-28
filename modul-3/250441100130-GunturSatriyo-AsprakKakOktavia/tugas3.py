kalimat = input("KASI KATA KATA DULU : ")

konsonan = 0
vokal = 0
huruf_vokal = "AIUEOaiueo"

for huruf in kalimat:
        if huruf in huruf_vokal:
            vokal += 1
        else:
            konsonan += 1

jumlah_kata = len(kalimat.split())

print("Kalimat :", kalimat)
print("Jumlah huruf konsonan :", konsonan)
print("Jumlah huruf vokal    :", vokal)
print("Jumlah kata           :", jumlah_kata)
