kalimat = input("Masukkan sebuah kalimat: ")

vokal = 0
konsonan = 0
kata = 0

huruf_vokal = "aiueoAIUEO"

di_dalam_kata = False

for huruf in kalimat:
    if ('A' <= huruf <= 'Z') or ('a' <= huruf <= 'z'):
        if huruf in huruf_vokal:
            vokal += 1
        else:
            konsonan += 1
        
        if not di_dalam_kata:
            kata += 1
            di_dalam_kata = True
    else:
        di_dalam_kata = False

print("\n=== HASIL ANALISIS KALIMAT ===")
print("Kalimat:", kalimat)
print("Jumlah huruf vokal    :", vokal)
print("Jumlah huruf konsonan :", konsonan)
print("Jumlah kata           :", kata) 