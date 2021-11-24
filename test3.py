jumlah_operasi = int(input("Masukkan banyak operasi: "))
for i in range(jumlah_operasi):
	operasi = input("Masukkan operasi: ")
	list_operasi = operasi.split()
	if 'BELI' == list_operasi[0]:
		beli_keranjang(list_operasi[1], list_operasi[2])
		print("Berhasil menambahkan {} dengan kapasitas {}".format(daftar_keranjang[0][0], daftar_keranjang[0][1]))
