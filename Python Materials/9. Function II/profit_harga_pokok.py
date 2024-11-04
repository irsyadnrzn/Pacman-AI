import produksi

produk = {
    'biaya_produksi':35000,
    'harga_jual':50000,
    'jumlah_produk':1200,
    'persediaan_sisa':100
}

produksi.harga_pokok_penjualan(produk['jumlah_produk'], produk['biaya_produksi'],produk['persediaan_sisa'])
produksi.keuntungan_penjualan(produk['jumlah_produk'], produk['harga_jual'], produk['biaya_produksi'])