print("="*10, " TUGAS 3 MODUL 6 ", "="*10)
angka_list = []

while True:
    print("\n--- PROGRAM PEMERIKSA ANGKA ---")
    print("1. Tambah angka")
    print("2. Tampilkan angka")
    print("3. Ubah angka")
    print("4. Hapus angka")
    print("5. Cek apakah bisa dibagi dua bagian sama jumlah")
    print("6. Keluar")

    pilih = input("Pilih menu (1-6): ")
    if pilih == "1":
        angka = int(input("Masukkan angka: "))
        angka_list.append(angka)
        print("Angka ditambahkan.")
    elif pilih == "2":
        print("Daftar angka:", angka_list)
    elif pilih == "3":
        if not angka_list:
            print("Belum ada angka untuk diubah.")
        else:
            print("Daftar angka sekarang:", angka_list)
            angka_lama = int(input("Masukkan angka yang ingin diubah: "))
            
            if angka_lama in angka_list:
                angka_baru = int(input("Masukkan angka pengganti: "))
                posisi = angka_list.index(angka_lama)
                angka_list[posisi] = angka_baru
                print(f"Angka {angka_lama} berhasil diubah menjadi {angka_baru}.")
            else:
                print("Angka tersebut tidak ditemukan di dalam daftar.")
    elif pilih == "4":
        if not angka_list:
            print("Belum ada angka yang bisa dihapus.")
        else:
            print("Daftar angka sekarang:", angka_list)
            angka_hapus = int(input("Masukkan angka yang ingin dihapus: "))
            if angka_hapus in angka_list:
                angka_list.remove(angka_hapus)
                print(f"Angka {angka_hapus} berhasil dihapus.")
            else:
                print("Angka tersebut tidak ada dalam daftar.")      
    elif pilih == "5":
        if not angka_list:
            print("Belum ada angka di dalam daftar.")
        else:
            print("Daftar angka:", angka_list)
            
            total = sum(angka_list)
            print(f"Jumlah total semua angka adalah: {total}")        
            if total % 2 != 0:
                print("Tidak bisa dibagi dua bagian sama besar karena jumlahnya ganjil.")
            else:
                setengah = total // 2
                print(f"Setengah dari total adalah: {setengah}")
                
                jumlah_sementara = 0
                bisa_dibagi = False
                
                for angka in angka_list:
                    jumlah_sementara += angka
                    if jumlah_sementara == setengah:
                        bisa_dibagi = True
                        break
                if bisa_dibagi:
                    print("Daftar bisa dibagi dua bagian dengan jumlah sama.")
                else:
                    print(" Tidak bisa dibagi dua bagian dengan jumlah sama.")


    elif pilih == "6":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!")



