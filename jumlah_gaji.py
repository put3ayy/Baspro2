# Input data pegawai
nama = input ("Masukkan Nama: ")
nik = input ("Masukkan NIK: ")
status = input ("Masukkan Status Pegawai (Tetap/Honor): ")
golongan = input ("Masukkan Golongan (A/B/C): ")

# Data gaji dan bonus
gaji_tetap = 1000000
gaji_honor = 750000
bonus_tetap = {'A': 200000, 'B': 400000, 'C': 550000}
bonus_honor = {'A': 150000, 'B': 275000, 'C': 480000}

#Menentukan gaji dan bonus
if status == "Tetap":
    gaji = gaji_tetap
    bonus = bonus_tetap.get(golongan, 0)
elif status == "Honor":
    gaji = gaji_honor
    bonus = bonus_honor.get(golongan, 0)
else:
    print("Status Pegawai Tidak Valid!")
    exit()

# Menghitung total gaji
gaji_total = gaji + bonus

# Output
print("\n======== Slip Gaji ========")
print("Nama             :", nama)
print("NIK              :", nik)
print("Status Pegawai   :", status)
print("Golongan         :", golongan)
print("Gaji Pokok       : Rp. ", gaji)
print("Bonus            : Rp. ", bonus)
print("Total Gaji       : Rp. ", gaji_total)
print("\n")
