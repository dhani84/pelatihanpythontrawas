kkm_sekolah = 75
nilai_ujian = int(input("Masukkan nilai ujian siswa: "))

if nilai_ujian >= kkm_sekolah:
    print("Status: TUNTAS")
    print("Siswa dapat mengikuti program pengayaan.")
else:
    print("Status: BELUM TUNTAS")
    print("Siswa dijadwalkan mengikuti remedial.")
