print("Silahkan masukkan nilai anda disini ya: ")
nilai = int(input())
if nilai >= 1 and nilai <= 100:
    if nilai >= 85 and nilai <= 100:
        print("Silhkan masukkan persentase kehadiran anda disini ya: ")
        kehadiran = int(input())
        if kehadiran >= 1 and kehadiran <= 100:
            print(str(nilai) + " nilai kamu A (SANGAT BAIK)")
            if kehadiran >= 90 and kehadiran <= 100:
                print("dan persentase kehadiranmu sangat baik juga")
                print("Selamat anda LULUS dengan pujian👍👍😊")
            else:
                print("Selamat anda LULUS")
    else:
        if nilai >= 70 and nilai <= 84:
            print(str(nilai) + " nilai kamu B(BAIK)")
        else:
            if nilai >= 60 and nilai <= 69:
                print(str(nilai) + " nilai kamu C (CUKUP)")
            else:
                if nilai >= 50 and nilai <= 59:
                    print(str(nilai) + " nilai kamu D (BURUK)")
                else:
                    print(str(nilai) + " nilai kamu E (BURUK SEKALI)")
                    print("Maaf ya anda TIDAK LULUS😒😒🤧")
                    print("Ayo jangan menyerah ya,,, semangat..👍😊")
