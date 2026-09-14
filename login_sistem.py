nama_pengguna = input("Masukkan Username: ")

# Pengecekan Lapis Pertama
if nama_pengguna == "admin_sekolah":
    kata_sandi = input("Username benar. Masukkan Password: ")
    
    # Pengecekan Lapis Kedua (Maju 1 Tab)
    if kata_sandi == "rahasia123":
        print("Akses disetujui. Selamat datang.")
    else:
        print("Password salah. Akses ditolak.")
else:
    print("Username tidak terdaftar di dalam sistem.")
