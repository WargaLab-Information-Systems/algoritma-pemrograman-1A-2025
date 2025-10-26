panjang= 10
lebar= 6
tinggi= 4

panjang= int(input("masukan panjang balok : "))
lebar= int(input("masukan lebar balok : "))
tinggi= int(input("masukan tinggi balok : "))

volume= (panjang * lebar * tinggi)
print("hasil volume baloknya adalah : ", volume)

luas_permukaan= 2 * (panjang * lebar) + (panjang * tinggi) + (lebar * tinggi)
print("jadi luas permukaan baloknya adalah : ", luas_permukaan, )