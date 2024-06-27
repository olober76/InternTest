def hitung_gaji(jam_kerja, tarif_per_jam):
    jam_normal = 40
    tarif_lembur = 1.5

    if jam_kerja > jam_normal:
        jam_lembur = jam_kerja - jam_normal
        gaji_normal = jam_normal * tarif_per_jam
        gaji_lembur = jam_lembur * tarif_per_jam * tarif_lembur
        gaji_total = gaji_normal + gaji_lembur
    else:
        gaji_total = jam_kerja * tarif_per_jam

    return gaji_total

def main():
    jam_kerja = float(input("Masukkan jumlah jam kerja: "))
    tarif_per_jam = float(input("Masukkan tarif per jam: "))

    gaji = hitung_gaji(jam_kerja, tarif_per_jam)

    print(f"Gaji karyawan adalah: Rp. {gaji:.2f}")

if __name__ == "__main__":
    main()
