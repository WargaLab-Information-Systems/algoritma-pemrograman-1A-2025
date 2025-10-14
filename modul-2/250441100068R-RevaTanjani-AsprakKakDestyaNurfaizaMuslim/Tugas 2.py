parkir= int(input("berapa lama parkir(jam):"))
status = (input("apakah ada kartu member VIP (ada/tidak): "))
# penyeleksian kondisi
if status == "ada":
    tarif = 0
elif parkir <= 2:
    tarif = 5000
elif parkir == 3:
    tarif = 8000
elif parkir == 4:
    tarif = 11000
elif parkir == 5:
    tarif = 14000
elif parkir == 6:
    tarif = 17000
elif parkir >= 7:
    tarif = 20000
    
#print
print("============================")
print("Member VIP: ",status)
print(f"Tarif: Rp {tarif}")
