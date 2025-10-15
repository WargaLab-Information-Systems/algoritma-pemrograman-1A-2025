kalimat = input("Masukkan kalimat: ")
vokal = 0
konsonan = 0
kata = len(kalimat.split())  # otomatis ngitung jumlah kata

for i in kalimat:
    if i.isalpha():  # biar cuma huruf yang dihitung
        if i.lower() in "aiueo":
            vokal += 1
        else:
            konsonan += 1

print("Jumlah kata adalah", kata)
print("Jumlah huruf vokal adalah", vokal)
print("Jumlah huruf konsonan adalah", konsonan)
