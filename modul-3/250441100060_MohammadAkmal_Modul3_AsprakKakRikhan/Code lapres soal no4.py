print("="*50)
print("          SELAMAT DATANG DI INDOMIE          ")
print("="*50)

ulang = 1
while ulang == 1:
    tanya = input("Apakah ada pembelian? (ya/tidak): ")
    if tanya == "tidak" or tanya == "TIDAK":
        print("Program selesai. Sampai jumpa!")
        ulang = 0
    else:
        nama = input("Nama pembeli: ")
        if nama == "":
            nama = "Pelanggan Umum"
        total = 0
        daftar = []
        print("\nMasukkan barang (ketik 'selesai' untuk berhenti):")
        jalan = 1
        while jalan == 1:
            brg = input("Nama barang: ")
            teks = ""
            for a in brg:
                if a != " ":
                    teks = teks + a
            if teks == "selesai" or teks == "SELESAI":
                jalan = 0
            else:
                h = input("Harga barang (Rp): ")
                cek = 1
                for x in h:
                    if x < "0" or x > "9":
                        cek = 0
                        break
                if cek == 0:
                    print("Harga harus berupa angka!")
                    continue
                angka = 0
                i = 0
                for digit in h:
                    angka = angka * 10 + int(digit)
                daftar = daftar + [{"nama": brg, "harga": angka}]
                total = total + angka
        
        print("="*50)
        print("           STRUK BELANJA           ")
        print("="*50)
        print("Nama Pembeli     :", nama)
        for d in daftar:
            print("-", d["nama"],       ": Rp", d["harga"])
        print("-----------------------------------")
        print("Total        : Rp", total)
        print("===================================")
        print("Terima kasih telah berbelanja di IndoMei!\n")