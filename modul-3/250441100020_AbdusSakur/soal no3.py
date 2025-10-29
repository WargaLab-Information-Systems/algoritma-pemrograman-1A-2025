vokal = "aiueo"
jumlahvokal = 0
jumlahkonsonan = 0

kalimat = input("masukan sebuah kalimat: ").lower()

for huruf in kalimat:
    if huruf.isalpha():
        if huruf in vokal:
            jumlahvokal += 1
        else:
            jumlahkonsonan += 1

jumlahkata = len(kalimat.split())

print(f"jumlah huruf vokal: {jumlahvokal}")
print(f"jumlah huruf konsonan: {jumlahkonsonan}")
print(f"jumlah kata dalam kalimat: {jumlahkata}")