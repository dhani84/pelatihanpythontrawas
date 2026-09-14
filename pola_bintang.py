tingkat = int(input("Masukkan jumlah baris pola: "))

# Perulangan luar: Mengatur jumlah baris vertikal
for baris in range(1, tingkat + 1):
    simbol = ""
    
    # Perulangan dalam: Mengisi kolom horizontal pada baris saat itu
    for kolom in range(baris):
        simbol = simbol + "★ "
        
    print(simbol)
