print(">> Menghidupkan Modul Kalkulator Usia Relatif")
tahun_referensi = 2026

# Menarik data dan mengonversinya secara instan menjadi perhitungan logis (Integer)
tahun_kelahiran = int(input("Masukkan parameter kalender lahir Anda (Contoh: 2011): "))

# Eksekusi matematika dengan operator pengurangan (-)
estimasi_usia = tahun_referensi - tahun_kelahiran

# Output laporan yang digabungkan menggunakan F-String
print(f"\n[Laporan] Berdasarkan algoritma, komputasi umur Anda saat ini adalah {estimasi_usia} tahun.")
