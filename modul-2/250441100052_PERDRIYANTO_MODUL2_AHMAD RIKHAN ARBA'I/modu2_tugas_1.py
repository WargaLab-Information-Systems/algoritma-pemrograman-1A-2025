print("Masukkan nilai anda ")
nilai = int(input())
print("Masukkan skor kehadiran")
kehadiran = int(input())
if nilai <= 100 and nilai >= 85:
    print("nilai anda A")
    print("anda lulus")
    if kehadiran <= 100 and kehadiran >= 90:
        print("Anda lulusan terbaik")
elif nilai <= 84 and nilai >= 70:
        print("nilai anda B")
elif nilai <= 69 and nilai >= 60:
        print("nilai anda C")
elif nilai <= 59 and nilai >= 50:
        print("nilai anda D")
elif nilai > 100 or nilai < 0 and kehadiran > 100 or kehadiran < 0:
    print("eror")
else:
    print("nilai anda E")
