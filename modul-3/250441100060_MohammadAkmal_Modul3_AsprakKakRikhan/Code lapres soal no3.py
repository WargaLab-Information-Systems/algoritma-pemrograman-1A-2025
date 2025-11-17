kal = input("Masukkan kalimat: ")

vok = 0
kon = 0
kata = 1

for char in kal:
    if char in 'aeiouAEIOU':
        vok = vok + 1
    elif char in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
        kon = kon + 1
    if char == ' ':
        kata = kata + 1

print("Jumlah vokal:", vok)
print("Jumlah konsonan:", kon)
print("Jumlah kata:", kata)