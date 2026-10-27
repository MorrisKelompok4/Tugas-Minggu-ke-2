def tambah(a, b):
    """Mengembalikan hasil penjumlahan a dan b"""
    return a + b

def kurang(a, b):
    """Mengembalikan hasil pengurangan a dan b"""
    return a - b

def kali(a, b):
    """Mengembalikan hasil perkalian a dan b"""
    return a * b

def bagi(a, b):
    """   Mengembalikan hasil pembagian a dan b.    Menangani pembagian error saat pembagi bernilai 0."""
    if b == 0:
        return "Error: Pembagi tidak boleh bernilai 0!"
    return a / b

def cek_ganjil_genap(angka):
    """   Memeriksa sifat bilangan ganjil atau genap menggunakan operator modulus (%) """
    if angka % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"

def hitung_deret_aritmatika(awal, beda, n):
    """  Menghitung total akumulasi deret menggunakan perulangan for """
    total = 0
    suku = awal 
    for i in range(n):
        total += suku
        suku += beda
    return total