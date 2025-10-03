harga_buku = 5000
pensil = 4500

total_buku = harga_buku*3
total_pensil = pensil*2
total = total_buku+total_pensil
print(f"total belana {total}")

pajak = 0.1
total_pajak = total*pajak
total_bayar = total-total_pajak
print(f"total setelah di pajak {total_bayar}")
