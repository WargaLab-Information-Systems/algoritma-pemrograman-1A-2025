print("="*15," Tugas 2 Program Mesin Atm ","="*15)
#Akses Masuk
sandi = 25012
kesempatan = 2
while kesempatan > 0:
    pin = int(input("Masukkan Pin ")) 
    if pin == sandi:
         print("pin benar akses di terima")
         break
    else:
        if len(str(pin)) > 5:
              print("pin lebih dari 5 ")
        elif len(str(pin))<5:
             print("Pin Kurang Dari 5 ")
        kesempatan -= 1
    if kesempatan == 0:
        print("Akses di blokir")
        break

# Menu menu
while kesempatan != 0:
    print('''-------------------- Menu Layanan ----------------------
        1. penarikan    2. transfer     3. Menu lainya\n''')
    user = int(input("Masukkan Pilihan Anda (1-3) : "))

    if user ==1:
         print(" 1. rekening tabungan 2. rekening giro ")
         user2 = int(input("Masukkan Pilihan Anda (1/2) : "))
         if user2 ==1:
              print("Permintaan Sedang Diproses")
              break
         else:
              print("Permintaan Sedang Diproses")
              break
    elif user ==2:
         print("\n 1. rekening 2. Dana ")
         user2 = int(input("Masukkan Pilihan Anda (1/2) : "))
         if user2 ==1:
              int(input("Masukkan Rekening Yang Akan Anda Transfer : "))
              print("Permintaan Sedang Diproses")
              break
         else:
              int(input("Masukkan Dana Yang Akan Anda Transfer : "))
              print("Permintaan Sedang Diproses")
              break
    else:
         print("\n 1. informasi saldo 2. keluar ")
         user2 = int(input("Masukkan Pilihan Anda (1/2) : "))
         if user2 ==1:
              print("Saldo Anda Sisa :   ")
              break
         else:
              print("\nTerimakasih Telah Mempercayai Kami ")
              break
         
              





