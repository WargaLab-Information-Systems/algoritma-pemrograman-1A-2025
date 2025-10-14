# while True:
#     n_input = input("Masukkan batas angka (n): ")

 
#     salah = False
#     for k in n_input:
#         if not ('0' <= k <= '9'):
#             salah = True
#             break

#     if salah or n_input == "":
#         print("Jangan masukkan huruf!")
#         continue


#     n = 0
#     for k in n_input:
#         n = n * 10 + (ord(k) - ord('0'))

#     print(f"\nBilangan prima dari 1 sampai {n} adalah:")


#     angka = 2
#     while angka <= n:
#         pembagi = 2
#         prima = True
#         while pembagi * pembagi <= angka:
#             if angka % pembagi == 0:
#                 prima = False
#                 break
#             pembagi += 1
#         if prima:
#             print(angka, end=" ")
#         angka += 1

#     print("\n")
#     break

for i in range(5):
    print(i+1)