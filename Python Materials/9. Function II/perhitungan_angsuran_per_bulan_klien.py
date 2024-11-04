def bunga_anuitas(pinjaman, bunga):
    hari = 30
    tabungan = pinjaman * bunga * hari
    return tabungan

def bunga_flat(pinjaman, bunga):
    bulan = 12
    bunga = bunga / 100
    pokok_pinjaman = pinjaman / bulan
    bunga_pertahun = pinjaman * bunga
    bunga_perbulan = bunga_pertahun / bulan
    total_angsuran = print(f"Angsuran perbulan yang wajib dibayarkan Rp.{int(pokok_pinjaman + bunga_perbulan)}")
    return total_angsuran