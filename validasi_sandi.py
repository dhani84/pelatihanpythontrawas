kata_sandi = ""

# Program akan terus bertanya selama sandi belum "KKA2026"
while kata_sandi != "KKA2026":
    kata_sandi = input("Masukkan kata sandi rahasia: ")
    
    if kata_sandi != "KKA2026":
        print("Sandi salah. Coba lagi.\n")

print("\nAkses disetujui. Selamat masuk ke sistem.")
