beras = 12000
gula = 14000
minyak = 20000 


diskon = 0
total_akhir = 0

print("Selamat datang di Toko Sembako “Maju Jaya”")
while True:
    jenis = input("Masukkan jenis barang (Beras, Gula, Minyak): ").lower()
    if jenis == "beras":
        banyak_barang= input("Masukkan berapa banyak barang: ")
        tot_beras = beras * int(banyak_barang)
        print(f"Subtotal adalah Rp.{tot_beras}")
        total_akhir += tot_beras
        if tot_beras > 150000:
            diskon = tot_beras * 0.1
            tot_beras = tot_beras - diskon
            print(f"Subtotal adalah Rp.{tot_beras}")
            total_akhir += tot_beras
            continue
    elif jenis == "gula":
        banyak_barang= input("Masukkan berapa banyak barang: ")
        tot_gula = gula * int(banyak_barang)
        print(f"Subtotal adalah Rp.{tot_gula}")
        total_akhir += tot_beras
        if tot_beras > 150000:
            diskon = tot_beras * 0.1
            tot_beras = tot_beras - diskon
            print(f"Subtotal adalah Rp.{tot_beras}")
            total_akhir += tot_beras
            continue
    elif jenis == "minyak":
        banyak_barang= input("Masukkan berapa banyak barang: ")
        tot_minyak = minyak * int(banyak_barang)
        print(f"Subtotal adalah Rp.{tot_minyak}")
        total_akhir += tot_beras
        if tot_beras > 150000:
            diskon = tot_beras * 0.1
            tot_beras = tot_beras - diskon
            print(f"Subtotal adalah Rp.{tot_beras}")
            total_akhir += tot_beras
            continue
    else:
        print("Masukkan input sesuai perintah")
        continue
    
    tanya = input("Apakah ada tambahan lagi? (y/n):").lower()
    if tanya != "y":
        break

while True:
    if total_akhir > 200000:
        diskon = total_akhir * 0.15
        total_akhir = total_akhir - diskon
    elif total_akhir > 100000:
        diskon = total_akhir * 0.1
        total_akhir = total_akhir - diskon

    member = input("Apakah pelanggan mempunyai member (y/n): ")
    if member == "y":
        diskon = total_akhir *0.05
        break
    else:
        diskon = 0
        break
        

print(f"Total akhir belanja pelanggan adalah: {total_akhir}")   
while True:
    lanjut = input("apakah ingin lanjut ke pelanggan selanjutnya? (y/n)")
    if lanjut != 'y':
        break