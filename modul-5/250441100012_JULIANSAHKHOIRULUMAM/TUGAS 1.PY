print("="*10," TUGAS 1 MODUL 5 ","="*10)

def faktorial(N):
    if N == 0 or N == 1:
        return 1
    else:
        return N * faktorial(N-1)
    
N = int(input("Masukkan Nilai N bilangan Bulat Non Negatif : "))

if N < 0:
    print("Nilai N Tidak Boleh Negatif. Coba Lagi.!!!")
    N = int(input("Masukkan Nilai N bilangan Bulat Non Negatif : "))
else:
    hasil = faktorial(N)
    print(f"faktorial Dari {N} Adalah {hasil}")