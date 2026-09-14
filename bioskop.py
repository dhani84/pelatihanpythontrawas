# Menetapkan batas umur
batas_umur = 13

umur_penonton = int(input("Berapa umur Anda? "))

# Hanya tampilkan ucapan ini jika umur mencukupi
if umur_penonton >= batas_umur:
    print("\nVerifikasi berhasil.")
    print("Selamat menonton film!")

print("Layanan tiket elektronik ditutup.")
