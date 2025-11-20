kupon = {
    'DISKON10': 10,
    'DISKON20': 20,
    'DISKON50': 50
} 

def menu():
    print("=== Menu Sistem Kasir ===")
    print("1. Tampilkan semua kupon tersedia")
    print("2. Proses transaksi")
    print("3. Keluar")

def kuponku():
    if not kupon:
        print("Tidak ada kupon tersedia.")
    else:
        print("Daftar Kupon Tersedia:")
        for kode, diskon in kupon.items():
            print(f"Kode: {kode}, Diskon: {diskon}%")

def transaksi():
    total_belanja_str = input("Masukkan total belanja: ").strip()
    
    if not total_belanja_str.replace('.', '', 1).isdigit():
        print("Input tidak valid! Total belanja harus berupa angka.")
        return
    
    total_belanja = float(total_belanja_str)
    if total_belanja < 0:
        print("Total belanja tidak boleh negatif.")
        return
    
    kode_kupon = input("Masukkan kode kupon: ").strip().upper()  
    
    if kode_kupon not in kupon:
        print("Kupon tidak valid atau sudah digunakan.")
        return
    
    persentase_diskon = kupon[kode_kupon]
    diskon = total_belanja * (persentase_diskon / 100)
    total_setelah_diskon = total_belanja - diskon
    
    print(f"Diskon diterapkan: {persentase_diskon}%")
    print(f"Jumlah diskon: Rp{diskon:.2f}")
    print(f"Total yang harus dibayar: Rp{total_setelah_diskon:.2f}")
    
    del kupon[kode_kupon]
    print("Kupon telah digunakan dan dihapus dari sistem.")

while True:
    menu()
    choice = input("Pilih opsi (1-3): ").strip()
    
    if choice == '1':
        kuponku()
    elif choice == '2':
        transaksi()
    elif choice == '3':
        print("Terima kasih telah menggunakan sistem kasir!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")