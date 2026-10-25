# ============================================================
# PROGRAM UTAMA: kalkulator.py
# Aplikasi Kalkulator Konsol Berbasis Menu Interaktif
# ============================================================

import operasi3  # Memanggil modul fungsi terpisah

while True:
    print("\n" + "=" * 45)
    print("       APLIKASI KALKULATOR KONSOL")
    print("=" * 45)
    print("1. Operasi Aritmatika Dasar (+, -, *, /)")
    print("2. Cek Sifat Bilangan (Ganjil / Genap)")
    print("3. Hitung Deret Aritmatika (For & Akumulator)")
    print("4. Cetak Tabel Perkalian Matriks (Nested Loop)")
    print("5. Keluar")
    print("=" * 45)

    pilihan = input("Pilih menu (1-5): ")

    # ----------------------------------------------------------
    # MENU 5: KELUAR PROGRAM
    # ----------------------------------------------------------
    if pilihan == "5":
        print("\nTerima kasih telah menggunakan Kalkulator Konsol. Program selesai!")
        break

    # ----------------------------------------------------------
    # MENU 1: OPERASI ARITMATIKA DASAR (+, -, *, /)
    # ----------------------------------------------------------
    elif pilihan == "1":
        print("\n--- Sub-Menu Operasi Dasar ---")
        print("A. Penjumlahan (+)")
        print("B. Pengurangan (-)")
        print("C. Perkalian (*)")
        print("D. Pembagian (/)")

        op = input("Pilih operasi (A/B/C/D): ").upper()