lama_parkir = int(input("Masukkan lama parkir (jam): "))
VIP = input("Apakah anda member VIP? (ya/tidak): ")

if VIP == "ya":
    biaya = 0   
    print("Anda member VIP (Gratis parkir)")
else:
    if lama_parkir <= 24:  
        if lama_parkir <= 2:
            biaya = 5000
        else:
            biaya = 5000 + (lama_parkir - 2) * 3000 + lama_parkir
            if biaya > 20000:   
                biaya = 20000   
    else:
        per_hari = lama_parkir // 24   
        jam = lama_parkir % 24  
        biaya = per_hari * 20000
        print("lama parkir dikali per hari")
        if jam == 0:
            pass 
        elif jam <= 12:
             biaya = jam  * 3000 + 20000   
        else:
            biaya = jam  * 3000 + 20000 

print("\n=== Hasil Perhitungan Parkir ===")
print(f"Lama parkir       : {lama_parkir} jam")
print(f"Status VIP        : {'Ya' if VIP == 'ya' else 'Tidak'}")
print(f"Total biaya parkir: Rp{biaya}")