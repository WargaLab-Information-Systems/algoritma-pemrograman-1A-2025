# Kasir Toko Sembako “Maju Jaya”

beras = 12000
gula = 14000
minyak = 20000
diskon = 0


while True :
    N = int(input("berapa banyak barang yanag kamu inginkan (beras)😊 :"))
    jumlah = ( beras * N )
    print (f"jadi total belanja anda untuk beras {jumlah}👍")
    i= int(input("berapa banyak barang yanag kamu inginkan (gula)😊 :"))
    jumlah = ( gula * i )
    print (f"jadi total belanja anda untuk gula {jumlah}👍")
    j = int(input("berapa banyak barang yanag kamu inginkan (minyak)😊 :"))
    jumlah = ( minyak * j )
    print (f"jadi total belanja anda untuk minyak {jumlah}👍")

    subtotal = (jumlah + jumlah + jumlah)

    member_card = str(input("Apakah anda tergolong sebagai member card(ya/tidak)"))
    if member_card.lower() == "ya" :
        diskon = +5
    print("Selamat anda mendapatkan tambahan diskon sebesar 5% 😊👌👌")
    total_belanja = jumlah + jumlah + jumlah * 5 / 100
    print (f"okey total belanja kalian adalah {total_belanja}")
    if subtotal >= 100 :
        diskon = 10
        total_belanja = jumlah + jumlah + jumlah * 10 / 100
        print (f"okey total belanja kalian adalah {total_belanja}")
    if subtotal >= 200 :
        diskon = 15 
        total_belanja = jumlah + jumlah +jumlah * 15 / 100
        print (f"okey total belanja kalian adalah {total_belanja}")
        
    perulangan = str(input("Apakah anda ingin mengulanginya (ya / tidak)"))
    if perulangan != "ya" :
        print ("TERIMAKASIH TELAH BERBELANJA DI TOKO KAMI TERCINTA “Maju Jaya”👌👌👌😊😊")
        break