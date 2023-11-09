#Nama : Bima Ady Zuana
#Kelas : 11 TKJ 2
#No Absen : 6
#Soal : Buatlah sebuah fungsi yang menghitung total dari deret bilangan ganjil hingga batas tertentu yang ditentukan pengguna.

def total_deret_ganjil(batas):
    total = 0
    for i in range(1, 2*batas,+ 1):
        bil_ganjil = 2 * i - 1
        total += bil_ganjil
    return total

batas = 10  
hasil = total_deret_ganjil(batas)
print(f"Total deret bilangan ganjil sampai {batas} adalah {hasil}")
