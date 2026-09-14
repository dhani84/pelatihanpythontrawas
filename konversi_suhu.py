# Fungsi fokus pada operasi aritmatika murni
def ubah_celcius_ke_fahrenheit(celcius):
    suhu_f = (celcius * 9/5) + 32
    return suhu_f  # Melempar angka hasil

# Alur Utama Program
suhu_ruangan = float(input("Berapa derajat celcius saat ini? "))

# Menangkap hasil lemparan (return) ke dalam wadah variabel baru
suhu_hasil = ubah_celcius_ke_fahrenheit(suhu_ruangan)

print(f"Apabila dikonversi, suhu ruangan adalah {suhu_hasil} Fahrenheit.")
