#Nama : Bima Ady Zuana
#Kelas : 11 TKJ 2
#No Absen : 6
#Soal : Buat program Python yang mengambil data penjualan bulanan produk dan menentukan kategori produk berdasarkan penjualan:
     #• Jika penjualan lebih dari 1000 unit, kategorikan sebagai "Produk Terlaris."
     #• Jika penjualan antara 500 hingga 1000 unit, kategorikan sebagai "Produk Populer."
     #• Jika penjualan kurang dari 500 unit, kategorikan sebagai "Produk Biasa."

penjualan_produk =float(input("Masukan jumlah penjualan pada bulan ini: "))

if  penjualan_produk > 1000:
    print("Produk terlaris") 
elif penjualan_produk >= 500:
    print("Produk Populer") 
else :
    print("Produk Biasa")

