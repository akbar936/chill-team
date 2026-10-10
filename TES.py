def tes_ganjil_genap():
    print("=== Tes Program Python Sederhana ===")
    try:
        # Meminta input angka dari pengguna
        angka = int(input("Masukkan sebuah angka: "))
        
        # Mengecek apakah angka ganjil atau genap
        if angka % 2 == 0:
            print(f"Angka {angka} adalah bilangan **Genap**.")
        else:
            print(f"Angka {angka} adalah bilangan **Ganjil**.")
            
    except ValueError:
        print("Input tidak valid! Harap masukkan angka.")

# Menjalankan fungsi
if __name__ == "__main__":
    tes_ganjil_genap()
