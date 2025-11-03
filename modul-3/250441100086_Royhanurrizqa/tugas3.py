kalimat=input("masukkan sebuah kalimat:").lower()

pisah_kata=kalimat.split()
total_kata=len(pisah_kata)

vokal="aiueo"
jumlah_vokal=0
jumlah_konsonan=0
for huruf in kalimat:
    if huruf.isalpha():
        if huruf in vokal:
            jumlah_vokal+=1
        else:
            jumlah_konsonan+=1

print("jumlah katanya adalah : ",total_kata)
print("jumlah huruf vokal adalah : ",jumlah_vokal)
print("jumlah huruf konsonan adalah : ",jumlah_konsonan)