kalimat = input("Masukkan sebuah kalimat: ").lower()

vokal = "aiueo"

jumlah_vokal = 0
jumlah_konsonan = 0

for i in kalimat:
    if i.isalpha():  
        if i in vokal:
            jumlah_vokal += 1
        else:
            jumlah_konsonan += 1

jumlah_kata = len(kalimat.split(" "))

print("Jumlah huruf vokal:", jumlah_vokal) 
print("Jumlah huruf konsonan:", jumlah_konsonan)
print("Jumlah kata:", jumlah_kata)
