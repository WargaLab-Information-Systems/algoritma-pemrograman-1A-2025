print("="*10," TUGAS 3 MODUL 5 ","="*10)

def hitung_gaji(nama, jabatan, gaji):
    pajak = 0.05 * gaji

    if jabatan.lower() == "manager":
        tunjangan = 0.10 * gaji
    elif jabatan.lower() == "staf":
        tunjangan = 0.05 * gaji
    else:
        tunjangan = 0

    gaji_bersih = (gaji-pajak)+ tunjangan

    print("-"*38)
    print("Nama Kariyawan         : ",nama)
    print("Jabatan Kariyawan      : ",jabatan)
    print(f"Gaji Pokok Kariyawan  : Rp.{gaji}",)
    print(f"Tunjangan Kariyawan   : Rp.{tunjangan}")
    print(f"Pajak Kariyawan       : Rp.{pajak}")
    print(f"Gaji Bersih Kariyawan : Rp.{gaji_bersih}")
    print("-"*38)

nama = input("Masukkan Nama Kriyawan : ").upper()
jabatan = input("Masukkan Jabatan (Manager/staf): ")
gaji = int(input("Masukkan Gaji Pokok Kariyawan : "))

hitung_gaji(nama, jabatan, gaji)