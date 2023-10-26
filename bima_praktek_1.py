#Nama : Bima Ady Zuana
#Kelas : 11 TKJ 2
#No Absen : 6
#Soal : Di toko online,hitung diskon berdasarkan total belanjaan pelanggan.

total_belanjaan = float(input("Total Belanjaan Anda: "))

if total_belanjaan > 500000:
    diskon = total_belanjaan * 0.10
elif total_belanjaan >= 300000:
    diskon = total_belanjaan * 0.05
else:
    diskon = 0

total_pembayaran = total_belanjaan - diskon
print(f"Total Pembayaran Setalah Diskon : {total_pembayaran}")
