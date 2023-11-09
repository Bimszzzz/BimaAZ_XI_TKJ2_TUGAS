#Nama : Bima Ady Zuana
#Kelas : 11 TKJ 2
#No Absen : 6
#Soal : Buatlah sebuah fungsi untuk menghitung faktorial dari suatu bilangan.

def fac(b):
    if b == 0:
        return 1
    else :
        return b * fac(b - 1)

b = 5  
hasil = fac(b)
print(f"Faktorial dari {b} adalah {hasil}")
