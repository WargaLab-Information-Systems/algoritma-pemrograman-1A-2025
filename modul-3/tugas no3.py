print("=== Program Analisa Kalimat ===")

kalimat = input("Masukkan sebuah kalimat: ")

vokal = 0
konsonan = 0

huruf_vokal = "aiueoAIUEO"

for huruf in kalimat:
    if huruf in huruf_vokal:
        vokal = vokal + 1
    elif huruf != " ":
        konsonan = konsonan + 1
 
spasi = 0
for huruf in kalimat:
    if huruf == " ":
        spasi = spasi + 1
jumlah_kata = spasi + 1

print("Jumlah huruf vokal   :", vokal)
print("Jumlah huruf konsonan:", konsonan)
print("Jumlah kata          :",jumlah_kata)