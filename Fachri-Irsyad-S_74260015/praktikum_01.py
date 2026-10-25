#==========================
# PRAKTIKUM 1:NESTED IF (EVALUASI KELULUSAN)
#Simpan sebagai: praktikum_01.py
#==========================

kehadiran = int(input("Jumlah kehadiran (1-14): "))
nilai = int(input("Nilai ujian (1-100): "))

if kehadiran >= 12:
    if nilai >= 75:
        print("Lulus - Nilai Memuaskan")
    else:
        print("REMEDIAL KAU")
else:
    print("TIDAK LULUS KAU BODO")