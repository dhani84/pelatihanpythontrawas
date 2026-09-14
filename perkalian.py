angka_dasar = int(input("Masukkan angka perkalian: "))

print(f"--- Tabel Perkalian {angka_dasar} ---")

for i in range(1, 11):
    hasil = angka_dasar * i
    print(f"{angka_dasar} x {i} = {hasil}")
