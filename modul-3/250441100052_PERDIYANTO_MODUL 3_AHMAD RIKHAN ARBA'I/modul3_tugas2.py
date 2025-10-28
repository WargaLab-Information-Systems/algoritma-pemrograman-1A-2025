pwd = 25052
batas = 3
x = 1
while x > 0 :
    print("1. login")
    print("2. Ganti password")
    print("3. exit")
    pilihan = input("masukkan pilihan 1/2/3 ")
    if pilihan == "2":
        baru = (input("masukkan pin baru "))
        pwd = baru
        continue
    else:
        x -= 1

while batas > 0:
    if pilihan == "1":
        user = (input("masukkan PIN "))
        if user == pwd:
            print("Pin benar, akses di terima ")
            break
        else:
            if len(str(user)) > 5:
                print("PIN lebih PIN harus 5 digit sedangkan pin anda ", len(str(user)))
            elif len(str(user)) < 5:
                print("PIN kurang PIN harus 5 digit sedangkan pin anda ", len(str(user)))
            batas -= 1
        print("Pin salah, coba lagi. kesempatan tinggl", batas)
        if batas == 0:
            print("akses di tolak, kartu di blokir")