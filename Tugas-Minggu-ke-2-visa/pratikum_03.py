# ================================================
# PRAKTIKUM 3: DERET ARITMATIKA & AKUMULATOR
# Simpan sebagai: praktikum_03.py
# ================================================

print ("=== PROGRAM HITUNG DERET ARITMATIKA ===")

awal = int(input("Masukan Suku Pertama (a):"))
beda = int(input("Masukan Beda Deret    (b):"))

# 1. IMPLEMENTASI WHILE: Validasi input jumlah suku agar harus positif (> 0)
banyak = int(input("Masukan Banyak Suku (n): "))
while banyak <= 0:
    print("Peringatan: Banyak suku harus lebuih dari 0!")
    banyak = int(input ("silahkan masukan ulang banyak  suku (n):"))

 # 2. IMPLEMENTASI FOR & AKUMULATOR: Mencetak deret dan menjumlahkan totalnya 
suku = awal
total = 0   # Celangan Akumulator

print("Barisan Deret: ", end="")
for i in range(banyak):
    print(suku, end=" ")
    total += suku     # Akumulasi penjumlahan bertahap
    suku += beda      # Menyiapkan suku berikutnya

print(f"\nTotal Deret: {total}")