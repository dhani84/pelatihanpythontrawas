def modul_ai_penjurusan(bakat):
    if bakat == "Logika":
        return "Klub Robotika KKA siap menampung bakat Anda."
    elif bakat == "Fisik":
        return "Tim Basket Sekolah menanti kehadiran Anda."
    else:
        return "Silakan konsultasi lebih lanjut dengan Guru Bimbingan Konseling."

print("=== Asisten Pendaftaran Ekstrakurikuler ===")
nama_siswa = input("Identitas Siswa: ")
bakat_utama = input("Bidang dominan (Logika/Fisik): ")

# Pemrosesan logika secara terpisah dari input
hasil_rekomendasi = modul_ai_penjurusan(bakat_utama)

print(f"\nRingkasan Evaluasi untuk {nama_siswa}:")
print(hasil_rekomendasi)
