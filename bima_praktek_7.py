#Nama : Bima Ady Zuana
#Kelas : 11 TKJ 2
#No Absen : 6
#Soal : Buat program Python yang mengambil informasi pembaruan perangkat lunak dan menentukan apakah sistem perlu di-restart. Jika pembaruan mengharuskan restart, program harus mencetak "Sistem perlu di-restart." Jika tidak, program harus mencetak "Sistem tidak perlu di-restart."

perlu_restart = input("Apakah PC atau Laptop anda perlu direstart? (iya/tidak): ")

if perlu_restart.lower() == "iya":
    print("Pc atau Laptop di-restart.")
else:
    print("Pc atau Laptop tidak perlu di-restart.")