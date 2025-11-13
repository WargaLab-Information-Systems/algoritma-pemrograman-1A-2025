def fungsi_faktorial(angka):
    faktoriaial = 1
    for i in range(1, angka + 1):
        faktoriaial =  faktoriaial * i
    return faktoriaial

while True:
    masukan = int(input("masukan angka lebih dari 0 (positif) "))
    if masukan < 0:
        print("angka harus lebih dari 0")
    else:
        break

print(f"hasil faktorrial dari {masukan} adalah = {fungsi_faktorial(masukan)}")