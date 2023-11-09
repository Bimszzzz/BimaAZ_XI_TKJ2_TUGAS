# Nama  :Bima Ady Zuana /06
# Kelas :11 TKJ 2
#Soal   :Deskripsi Pekerjaan: Seorang pedagang memiliki 100 buah apel. Setiap harinya, ia menjual 10% dari jumlah apel yang tersisa. Buatlah program yang menghitung berapa hari yang dibutuhkan agar sisa apel kurang dari 20 buah.

Awal_buah_apel = 100
Target_sisa = 20
Hari = 0

while Awal_buah_apel > Target_sisa :
    Awal_buah_apel = Awal_buah_apel - 0.10 * Awal_buah_apel
    Hari += 1
    print(f"Sisa apel {Awal_buah_apel} pada hari ke {Hari}")

print(f"Membutuhkan {Hari} hari agar apel mencapai 20")