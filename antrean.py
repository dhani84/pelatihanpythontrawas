jumlah_peserta = int(input("Berapa peserta yang hadir? "))

print("\nMemulai pencetakan nomor antrean...")

# Tambahkan +1 agar hitungan berhenti tepat di angka jumlah_peserta
for urutan in range(1, jumlah_peserta + 1):
    print(f"Mencetak Tiket: {urutan}")

print("Pencetakan selesai.")
