def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

while True:
    try:
        input_angka = int(input("Masukkan angka untuk menghitung faktorial: "))
        if input_angka < 0:
            print("Angka harus bilangan bulat positif")
        else:
            hasil = faktorial(input_angka)
            print(f"Faktorial dari {input_angka}! adalah {hasil}")
            break
    except:
        print("Input Harus angka!!")