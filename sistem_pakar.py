# --- BLOK MESIN INFERENSI KECERDASAN ARTIFISIAL ---

def mesin_inferensi_minat(logika, fisik, seni):
    # Evaluasi kombinasi multivariabel menggunakan operator 'and'
    if logika == "Ya" and fisik == "Tidak" and seni == "Tidak":
        return "Rekomendasi Mutlak: Klub Pemrograman & Robotika."
    elif logika == "Tidak" and fisik == "Ya" and seni == "Tidak":
        return "Rekomendasi Mutlak: Akademi Olahraga (Atletik/Basket)."
    elif logika == "Tidak" and fisik == "Tidak" and seni == "Ya":
        return "Rekomendasi Mutlak: Sanggar Kesenian & Teater."

   # Analisis Hibrida (Kombinasi 2 Minat)
    elif logika == "Ya" and fisik == "Ya" and seni == "Tidak":
        return "Rekomendasi Hibrida: Klub Esport atau Desain Rekayasa Mekanik."
    elif logika == "Ya" and fisik == "Tidak" and seni == "Ya":
        return "Rekomendasi Hibrida: Animasi Digital & Desain Grafis."
    
    # Titik akhir pencegahan galat logika (Fallback)
    else:
        return "Resolusi Terbuka: Membutuhkan asesmen lanjutan oleh Guru BK."

# --- BLOK PROGRAM UTAMA (ANTARMUKA) ---
print("=== AI KONSELOR DETEKSI MINAT SISWA ===")

status_sistem = True

while status_sistem == True:
    print("\n[Mulai Sesi Wawancara]")
    nama_siswa = input("Identitas Siswa: ")

    # Meminta respons biner (Ya/Tidak) di DALAM blok while
    print("Jawab pertanyaan berikut dengan 'Ya' atau 'Tidak':")
    tanya_1 = input("1. Apakah Anda menyukai pemecahan masalah matematika/puzzle? : ")
    tanya_2 = input("2. Apakah Anda menyukai aktivitas jasmani yang intens?         : ")
    tanya_3 = input("3. Apakah Anda memiliki ketertarikan pada musik atau visual?   : ")
    
    # Transmisi data menuju Fungsi AI
    hasil_resolusi = mesin_inferensi_minat(tanya_1, tanya_2, tanya_3)
