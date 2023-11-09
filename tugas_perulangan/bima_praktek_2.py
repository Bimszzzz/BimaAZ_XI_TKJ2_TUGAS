# Nama  :Bima Ady Zuana /06
# Kelas :11 TKJ 2
#Soal   :Deskripsi Pekerjaan: Seorang pelari ingin meningkatkan jarak tempuhnya setiap minggunya. Ia mulai dengan 5 kilometer dan meningkatkan jaraknya sebesar 10% setiap minggunya. Buatlah program yang menghitung berapa minggu yang dibutuhkan agar pelari itu dapat berlari lebih dari 10 kilometer.

Jarak_Awal = 5
Jarak_Target = 10
Minggu = 0

while Jarak_Awal < Jarak_Target :
    Jarak_Awal = Jarak_Awal + 0.10 * Jarak_Awal
    Minggu += 1
    print(f"Jarak{Jarak_Awal}kilometer pada minggu ke {Minggu}")

print(f"Dibutuhkan{Minggu}minggu untuk si pelari mencapai lebih 10 km")
