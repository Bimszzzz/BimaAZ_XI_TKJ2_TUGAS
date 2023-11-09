# Nama  :Bima Ady Zuana /06
# Kelas :11 TKJ 2
#Soal   :Deskripsi Pekerjaan: Sebuah bakteri pembelahan setiap 20 menit. Sebuah bakteri ditempatkan dalam lingkungan yang cocok dan berkembang biak dengan cepat. Buatlah program yang menghitung berapa kali pembelahan bakteri terjadi dalam rentang waktu 2 jam.

rentang_waktu = 120
pembelahan_membutuhkan_waktu_= 20
jumlah_pembelahan = 0

while pembelahan_membutuhkan_waktu_ <= rentang_waktu:
    rentang_waktu -= pembelahan_membutuhkan_waktu_
    jumlah_pembelahan += 1
    print(f'Bakteri melakukan penjumlahan sebanyak {jumlah_pembelahan} pada sisa {rentang_waktu} menit')
print(f'Dalam waktu 2 jam, bakteri mengalami pembelahan sebanyak {jumlah_pembelahan} kali.')