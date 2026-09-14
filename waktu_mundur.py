import time # Modul untuk memberikan jeda waktu

waktu_tersisa = int(input("Atur waktu mundur (detik): "))

while waktu_tersisa > 0:
    print(f"Waktu tersisa: {waktu_tersisa} detik")
    time.sleep(1) # Berhenti sejenak selama 1 detik
    
    # Kurangi waktu tersisa agar perulangan bisa berhenti
    waktu_tersisa = waktu_tersisa - 1 

print("Waktu habis!")
