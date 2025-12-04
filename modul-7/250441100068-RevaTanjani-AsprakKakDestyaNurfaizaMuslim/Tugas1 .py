kontak = {
    "Reno": ["@reno","0823"],
    "Nafis" : ["@nafis, 0897"]
}


while True:
    print("\n Silahkan pilih: 1.Tambah 2.Update 3.Hapus 4.daftar kontak 5.cari kontak")
    menu = input ("pilih: ")

    if menu == "1":
           print("menambah kontak")
           key = input("masukkan nama kontak:")
           value = input("masukkan email dan nomor(pisahkan dengan koma): ").split(",")
           kontak[key]= value
           print("\n===kontak berhasil ditambah===")

    elif menu == "2":
          print("mengupdate kontak")
          ganti= input("masukkan nama kontak yang ingin diupdate: ")

          if ganti in kontak:
                update = input("anda ingin mengupdate nama, email, nomor: ")
                if update == "nama":
                      NamaBaru = input("masukkan nama baru:  ")
                      kontak[NamaBaru]= kontak.pop[ganti]
                      print("\n===kontak berhasil diupdate===")

                elif update == "email":
                      kontak[ganti][0] = input("masukkan email baru: ")
                      print("\n===kontak berhasil diupdate===")

                elif update == "nomor":
                      Nomorbaru = input("masukkan nomor baru: ")

                      if Nomorbaru.isdigit():
                            kontak[ganti][1]= Nomorbaru
                            print("\n===Kontak berhasil diupdate===")

                      else:
                            print("masukan NOMORRR")

                elif update != "nomor" and update != "email" and update != "nomor":
                      print("\npilihan tersebut tidak ada")

          else:
                print("\nkontak tidak ditemukan")

    elif menu == "3":
          print("Menghapus kontak")
          hapus = input ("masukkan kontak yang ingin dihapus: ")

          if hapus in kontak:
                del kontak[hapus]
                print("\n====kontak berhasil dihapus====")
                
          else:
                print("\nkontak tidak tersedia")

    elif menu == "4":
          print("\n==========Daftar nama kontak==============")
          for daftar in kontak.items():
                print(daftar)
          print("Total kontak anda: ", len(kontak))

    elif menu == "5":
          print("Mencari kontak")
          cari = input("masukkan nama kontak yang dicari: ")

          if cari in kontak:
                print("\n===kontak ditemukan===")
                print(cari, ":", kontak[cari])

          else:
                print("\nKontak tidak ditemukan")
                
    else:
        print("\npilihan tidak ada, coba lagi")