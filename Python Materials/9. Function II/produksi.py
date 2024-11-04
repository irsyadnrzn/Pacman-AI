def keuntungan_penjualan(jumlah_produk, harga_jual, biaya_produksi):
    keuntungan = (jumlah_produk*harga_jual) - (jumlah_produk*biaya_produksi)
    return print(f"Profit yang didapatkan bulan ini adalah : {keuntungan}")

def harga_pokok_penjualan(jumlah_produk, biaya_produksi, persediaan_sisa):
    harga_pokok = biaya_produksi + jumlah_produk - persediaan_sisa
    return print(f"Harga pokok yang dikeluarkan adalah : {harga_pokok}")
