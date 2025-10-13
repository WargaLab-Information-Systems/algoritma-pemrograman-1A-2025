kalimat = input("Buatlah sebuah kalimat : ").lower()
vokal = "aiueo"
vokal1 = 0
konsonan = 0

for huruf in kalimat :
    if huruf.isalpha():
        if huruf in vokal:
            vokal1 += 1
        else :
            konsonan += 1
            
kata = kalimat.split()
kata1 = len(kata)

print("Jumlah huruf vokal :", vokal1)
print("Jumlah huruf konsonan : " , konsonan)
print("Jumlah kata dalam kalimat : ", kata1) 