kalimat = input("Masukkan kalimat: ").lower()

vokal = 0
konsonan = 0

for i  in kalimat:
    if 'a' >= i or i <= 'z':
        if i in 'aiueo':
            vokal += 1
        else:
            konsonan += 1

kata = len(kalimat.split())

print("Jumlah huruf vokal: ", vokal)
print("Jumlah huruf konsonan: ", konsonan)
print("Jumlah kata: ", kata)