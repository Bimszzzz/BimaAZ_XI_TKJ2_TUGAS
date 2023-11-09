#Nama : Bima Ady Zuana
#Kelas : 11 TKJ 2
#No Absen : 6
#Soal : Buatlah sebuah fungsi yang menghitung bilangan Fibonacci ke-n.

def fibo(n):
    if n <= 0:
        return
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n -1) + fibo(n -2)
    
n = 15
hasil = fibo(n)
print(f'Fibonanci ke-{n} adalah {hasil}')