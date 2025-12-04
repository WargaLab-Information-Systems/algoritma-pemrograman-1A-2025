Kalimat = input("Masukkan kalimat: ")

vokal = "aiueoAIUEO"
jumlah_vokal = 0
jumlah_konsonan = 0

for huruf in Kalimat:
    if huruf.isalpha(): #mengecek apakah alphabet
        if huruf in vokal:
            jumlah_vokal += 1
        else:
            jumlah_konsonan += 1
            
            
kata = Kalimat.split() #memisah spasi
jumlah_kata = len(kata) #menghitung elemen (kata)

print("Jumlah huruf vokal:", jumlah_vokal)
print("Jumlah huruf konsonan:", jumlah_konsonan)
print("Jumlah kata:", jumlah_kata)