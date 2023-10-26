#Nama : Bima Ady Zuana
#Kelas : 11 TKJ 2
#No Absen : 6
#Soal :Buat program Python yang mengambil estimasi waktu selesai proyek dan tanggal target selesai. Jika estimasi waktu selesai lebih awal atau sama dengan tanggal target, program harus mencetak "Tepat waktu," jika tidak, program harus mencetak "Terlambat.

estimasi_selesai = input("Estimasi Waktu Selesai Proyek (Tahun-Bulan-Hari): ")
tanggal_target = input("Tanggal Target Selesai (Tahun-Bulan-Hari): ")


# Periksa apakah estimasi selesai lebih awal atau sama dengan tanggal target
if estimasi_selesai <= tanggal_target:
    print("Tepat waktu")
else:
    print("Terlambat")
