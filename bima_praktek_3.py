#Nama : Bima Ady Zuana
#Kelas : 11 TKJ 2
#No Absen : 6
#Soal : Buat program Python yang memeriksa apakah suatu file sudah ada di direktori server. Jika file sudah ada, program harus mencetak "File sudah ada," jika tidak, program harus mencetak "File belum ada"

nama_file = "data.txt"
daftar_file_yang_ada_diserver = ["file1.txt", "file2.txt", "data.txt", "file3.txt"]

if nama_file in daftar_file_yang_ada_diserver:
    print("File ada")
else:
    print("File tidak ada")

