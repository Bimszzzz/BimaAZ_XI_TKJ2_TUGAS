#Nama : Bima Ady Zuana
#Kelas : 11 TKJ 2
#No Absen : 6
#Soal : Buat program Python yang mengambil durasi peminjaman buku dalam hari dan menentukan jenis pinjaman berdasarkan aturan berikut:
    #• Peminjaman 7 hari atau kurang: "Peminjaman Pendek"
    #• Peminjaman lebih dari 7 hari hingga 30 hari: "Peminjaman Menengah"
    #• Peminjaman lebih dari 30 hari: "Peminjaman Panjang"

peminjaman_diperpus = float(input("Memasukan lama pinjaman: "))
if peminjaman_diperpus <=7:
    print("Pinjaman jangka pendek")
elif peminjaman_diperpus >30:
    print("Pinjaman jangka panjang")
else:
    print("Pinjaman jangka menengah")