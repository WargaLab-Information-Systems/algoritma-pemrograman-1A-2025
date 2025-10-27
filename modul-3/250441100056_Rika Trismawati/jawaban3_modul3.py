
kalimat = input("Masukkan Kalimat: ")

vocal = 0
konsonan = 0

for huruf in kalimat:
    if huruf in  "aiueoAIUEO":
        vocal = vocal + 1
    elif huruf.isalpha():
        konsonan = konsonan + 1

kata = kalimat.split()
print("vocal =", vocal)
print("konsonan", konsonan)
print("jumlah kata =", len(kata))


