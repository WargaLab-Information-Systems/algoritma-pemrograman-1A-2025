pin = "25150"
maksimal_coba = 3

print("Selamat datang di ATM")

for i in range(maksimal_coba):
    user_input = input(f"Masukkan PIN (percobaan {i+1}/{maksimal_coba}): ")

    try:
        _ = user_input[5] 
        print("PIN harus 5 digit. Coba lagi.")
        
        if i == maksimal_coba - 1:
            print("Akses ditolak, kartu diblokir.")
        continue

    except IndexError:
        pass
    
    try:
        int(user_input) 

        if user_input == pin:
            print("PIN benar, akses diterima!")
            break

        if i < maksimal_coba - 1:
            print("PIN salah, coba lagi.")
        else: 
            print("Akses ditolak, kartu diblokir.")

    except ValueError as error:
        if str(error) == "PIN terlalu pendek":
             print("PIN harus 5 digit. Coba lagi.")
        else:
             print("PIN harus berupa angka. Coba lagi.")
        if i == maksimal_coba - 1:
             print("Akses ditolak, kartu diblokir.")