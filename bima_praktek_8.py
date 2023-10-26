#Nama : Bima Ady Zuana
#Kelas : 11 TKJ 2
#No Absen : 6
#Soal : Buat program Python yang mengambil status persiapan proyek dan menentukan apakah proyek tersebut dapat diluncurkan. Jika status persiapan "Siap," program harus mencetak "Proyek diluncurkan." Jika status persiapan "Tunda," program harus mencetak "Proyek ditunda."

persiapan_proyek = input("Apakah proyek sudah siap untuk diluncurkan? (siap/belum): ")

if persiapan_proyek.lower() == "siap":
    print("Proyek sudah siap untuk diluncurkan.")
else:
    print("Proyek belum siap untuk diluncurkan.")