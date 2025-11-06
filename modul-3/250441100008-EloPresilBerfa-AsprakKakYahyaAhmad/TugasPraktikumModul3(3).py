print("="*50)
print("Nama : Elo Presil Berfa")
print("NIM : 250441100008")
print("="*50)

#Soal

#Buatlah program yang meminta user untuk memasukkan sebuah kalimat. Lalu program akan menganilsa kalimat tersebut dan menampilkan :
#a. Jumlah huruf vokal dan konsonan
#b. Jumlah kata dalam kalimat

#Jawaban

n = input("Input Kalimat : ").lower()

vokal = 0
konsonan = 0
kata = 0
sebelum_spasi = False

huruf_kecil = "abcdefghijklmnopqrstuvwxyz"

for i in n:
    ada = False
    for j in huruf_kecil:
        if i == j:
            ada = True

    if ada:
        if i == 'a' or i == 'i' or i == 'u' or i == 'e' or i == 'o':
            vokal = vokal + 1
        else:
            konsonan = konsonan + 1

    if i != ' ' and not sebelum_spasi:
        kata += 1
        sebelum_spasi = True
    elif i == ' ':
        sebelum_spasi = False
        
if vokal > 0:
    print('Jumlah huruf vokal :', vokal)
else:
    print('Huruf vokal tidak ditemukan')

if konsonan > 0:
    print('Jumlah huruf konsonan :', konsonan)
else:
    print('Huruf konsonan tidak ditemukan')

print('Jumlah kata :', kata)


print("="*50)


