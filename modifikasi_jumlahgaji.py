# Data gaji dan bonus
gaji_tetap = 1000000
gaji_honor = 750000

bonus_tetap = {'A': 200000, 'B': 400000, 'C': 550000}
bonus_honor = {'A': 150000, 'B': 275000, 'C': 480000}

# Data status dan golongan
status_pegawai = ["Tetap", "Honor"]
golongan_pegawai = ["A", "B", "C"]

print("\n======== Daftar Slip Gaji ========")

# Perulangan untuk setiap status pegawai dan golongan
for status in status_pegawai:
    if status == "Tetap":
        gaji_pokok = gaji_tetap
        bonus_data = bonus_tetap
    else:
        gaji_pokok = gaji_honor
        bonus_data = bonus_honor

    # Perulangan untuk setiap golongan
    for golongan in golongan_pegawai:
        bonus = bonus_data[golongan]
        gaji_total = gaji_pokok + bonus

        # Menampilkan output lengkap dalam satu blok
        print("\nStatus Pegawai :", status)
        print("Golongan         :", golongan)
        print("Gaji Pokok       : Rp.", gaji_pokok)
        print("Bonus            : Rp.", bonus)
        print("Total Gaji       : Rp.", gaji_total)

print("\n")