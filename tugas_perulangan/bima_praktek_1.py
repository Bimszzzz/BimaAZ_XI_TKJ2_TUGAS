# Nama  :Bima Ady Zuana /06
# Kelas :11 TKJ 2
#Soal   :Seorang petani memiliki 100 ekor ayam di peternakannya. Setiap bulan, jumlah ayam bertambah 5% dari jumlah ayam pada bulan sebelumnya. Buatlah program yang menghitung berapa bulan yang dibutuhkan agar jumlah ayam melebihi 200 ekor.

Jumlah_Ayam = 100
Target_Ayam = 200
Bulan = 0

while Jumlah_Ayam < Target_Ayam:
    Bulan += 1
    bertambahnya_ayam = Jumlah_Ayam * 0.05 
    Jumlah_Ayam += bertambahnya_ayam
    print(f"Pertumbuhan ayam {Jumlah_Ayam} pada bulan ke {Bulan}")

print(f"Kita membutuhkan {Bulan} bulan untuk melebihi jumlah ayam{Target_Ayam} ekor.")