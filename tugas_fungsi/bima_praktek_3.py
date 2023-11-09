#Nama : Bima Ady Zuana
#Kelas : 11 TKJ 2
#No Absen : 6
#Soal : Buatlah sebuah fungsi yang menghitung nilai pangkat dari suatu bilangan dengan eksponen tertentu.

def menghitung_pangkat(bilangan, eksponen):
        
    hasil = bilangan ** eksponen
    return hasil

bilangan = 7
eksponen = 8  
hasil = menghitung_pangkat(bilangan, eksponen)
print(f"Hasil pangkat dari {bilangan} dengan eksponen {eksponen} adalah {hasil}")
