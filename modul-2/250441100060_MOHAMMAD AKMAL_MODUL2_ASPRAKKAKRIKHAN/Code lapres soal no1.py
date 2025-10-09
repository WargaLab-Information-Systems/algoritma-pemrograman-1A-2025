print("silahkan masukkan nilai anda disini untuk menentukan simbol pada nilai anda")
nilai = int(input())
print("Masukkan presentase kehadiran anda")
kehadiran = int(input())
if nilai >= 100:
    print("nilai anda tidak valid")
else:
    if nilai >= 85:
        print(str(nilai) + " Nilai kamu bagus A")
        if kehadiran >= 90:
            print("Selamat kamu masuk kategori mahasiswa terbaik")
    else:
        if nilai >= 70 and nilai <= 84:
            print(str(nilai) + " nilai kamu B(baik)")
        else:
            if nilai >= 60 and nilai <= 69:
                print(str(nilai) + " nilai kamu C (cukup)")
            else:
                if nilai >= 50 and nilai <= 59:
                    print(str(nilai) + " nilai kamu D (buruk)")
                else:
                    if nilai <= 0:
                        print("nilai anda tidak memenuhi syarat")
                    else:
                        print(str(nilai) + " nilai kamu (E) buruk sekali")
                        print("kamu tidak lulus harus ngulang lagi tahun depan")
