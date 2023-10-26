<<<<<<< HEAD
#Nama : Bima Ady Zuana
#Kelas : 11 TKJ 2
#No Absen : 6
#Soal : Buat program Python yang mengambil nilai performa karyawan (1 hingga 5, dengan 5 sebagai performa terbaik) dan menghitung bonus tahunan berdasarkan aturan berikut:
    #• Performa 5: Bonus 20% dari gaji tahunan.
    #• Performa 4: Bonus 10% dari gaji tahunan.
    #• Performa 3: Bonus 5% dari gaji tahunan.
    #• Performa 2: Bonus 2% dari gaji tahunan.
    #• Performa 1: Tidak ada bonus.
#Buatlah program menggunakan percabangan ternary untuk menghitung bonus tersebut.

performa = float(input("Masukan peforma karyawan kalian (dari 1 - 5): "))
gaji = float(input("Gaji karyawan dalam setahun ini: "))

if performa == 5:
    bonus = gaji * 0.20
elif performa == 4:
    bonus == gaji * 0.10
elif performa == 3:
    bonus = gaji * 0.05
elif performa == 2:
    bonus = gaji * 0.02
else:
    bonus = 0
total_gaji = bonus = gaji
=======
#Nama : Bima Ady Zuana
#Kelas : 11 TKJ 2
#No Absen : 6
#Soal : Buat program Python yang mengambil nilai performa karyawan (1 hingga 5, dengan 5 sebagai performa terbaik) dan menghitung bonus tahunan berdasarkan aturan berikut:
    #• Performa 5: Bonus 20% dari gaji tahunan.
    #• Performa 4: Bonus 10% dari gaji tahunan.
    #• Performa 3: Bonus 5% dari gaji tahunan.
    #• Performa 2: Bonus 2% dari gaji tahunan.
    #• Performa 1: Tidak ada bonus.
#Buatlah program menggunakan percabangan ternary untuk menghitung bonus tersebut.

performa = float(input("Masukan peforma karyawan kalian (dari 1 - 5): "))
gaji = float(input("Gaji karyawan dalam setahun ini: "))

if performa == 5:
    bonus = gaji * 0.20
elif performa == 4:
    bonus == gaji * 0.10
elif performa == 3:
    bonus = gaji * 0.05
elif performa == 2:
    bonus = gaji * 0.02
else:
    bonus = 0
total_gaji = bonus = gaji
>>>>>>> 450114d565d4fdec17eef0de635f8bcf53e0d400
print(f"Total gaji setahun dari karyawan kalian: {total_gaji}")