kalimat = input("Tulis kalimat anda ")
vokal = 0
konsonan = 0
kata = 1
for huruf in kalimat:
    if huruf == " ":
        kata += 1
    elif huruf in "aiueoAIUEO":
        vokal += 1
    elif huruf != " ":
        konsonan += 1
print("Jumlah huruf vokal:", vokal)
print("Jumlah huruf konsonan:", konsonan)
print("Jumlah kata:", kata)