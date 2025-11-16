# # # Soal Nomor 3
# # # Pola Piramida Simetris (dibalik dari bawah ke atas)
# # # Menggunakan pola dan struktur perulangan (nested loop)

# # n = int(input("Masukkan nilai n: "))

# for i in range(n, 0, -1):  
    
#     for j in range(1, i + 1):
#         print(j, end=" ")

#     if i == n: 
#         spasi = 0 
#     else:
#         spasi = (n - i) * 4 
#     print(" " * spasi, end="")

#     for k in range(i, 0, -1): 
#         print(k, end=" ")

#     print()  

# n=int(input("Masukkan pola bintang:"))

# for i in range(1, n + 1):
    
#     for j in range(1, i + 1):
#         print(" "* (n - i), end="")
#         print("*" * (2 * i - 1))







# Soal Nomor 3
# Pola Piramida Simetris (dibalik dari bawah ke atas)
# Menggunakan pola dan struktur perulangan (nested loop)


# # Soal Nomor 3
# # Pola Piramida Simetris (dibalik dari bawah ke atas)
# # Menggunakan pola dan struktur perulangan (nested loop)

n = int(input("Masukkan tinggi setengah pola: "))

for i in range(1, n + 1):  
    print(" "* (n - i), end="")
    print("*" * (2 * i - 1))

for i in range(n - 1, 0,-1):
    print (" " * (n - i), end="")
    print("*" * (1 * i - 1))


































