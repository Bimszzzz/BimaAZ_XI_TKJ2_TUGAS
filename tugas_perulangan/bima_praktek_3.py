# Nama  :Bima Ady Zuana /06
# Kelas :11 TKJ 2
#Soal   :Deskripsi Pekerjaan: Sebuah investasi awal sebesar 10.000 dollar tumbuh sebesar 6% setiap tahunnya. Buatlah program yang menghitung berapa tahun yang dibutuhkan agar nilai investasi melebihi 20.000 dollar.

Investasi_awal = 10000
Target_Investasi = 20000
Tahun = 0

while Investasi_awal < Target_Investasi :
    Investasi_awal = Investasi_awal + 0.06 * Investasi_awal
    Tahun += 1
print(f"Nilai investasi {Investasi_awal} pada tahun ke {Tahun}")

print(f"Membutuhkan berapa {Tahun} tahun agar investasi mencapai target 20.000 dollar")