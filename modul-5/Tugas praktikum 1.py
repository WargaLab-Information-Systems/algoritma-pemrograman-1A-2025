# Fungsi rekursif untuk menghitung faktorial
def fk (n):
   if n == 0:  # basis rekursi
      return 1
   else:
      return n * fk (n - 1) #memanggil dgn rekursi
n = int(input("masukkan bilangan faktorial = "))
if n < 0:
   print(f"{n} ! = bilangan bukan faktorial")
else:
   print(f"{n}! = ", fk(n))
