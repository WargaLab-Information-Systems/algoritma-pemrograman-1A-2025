halim_membeli_buku_tulis_sebanyak= 3
halim_membeli_pensil_sebanyak= 2
harga_satuan_buku_tulis= 5.000
harga_satuan_pensil= 4.500
pajak_pembelian= 0.10

total_harga= (halim_membeli_buku_tulis_sebanyak * harga_satuan_buku_tulis) + (halim_membeli_pensil_sebanyak * harga_satuan_pensil)
print("total harganya : Rp.", total_harga)

pajak= (float(pajak_pembelian * total_harga))
print("terkena pajak pembelian sebesar : Rp.", pajak)

setelah_pajak= (float(pajak + total_harga))
print("jadi total harga berserta pajaknya adalah : Rp.", setelah_pajak)