from lingkaran import luas_lingkaran, keliling_lingkaran
from persegi_panjang import luas_persegi_panjang, keliling_persegi_panjang
from segitiga import luas_segitiga, keliling_segitiga

print("===============================================================================")
bangun_datar = input("Apa yang ingin anda hitung (lingkaran/persegi panjang/segitiga) : ")
hitung = input("Luas/keliling : ")

bangun_datar = bangun_datar.title()
hitung = hitung.title()

if bangun_datar == 'Lingkaran':
    if hitung == 'Luas':
        luas = luas_lingkaran()
        print(luas)
    elif hitung == 'Keliling':
        keliling = keliling_lingkaran()
        print(keliling)
    else:
        print('Input tidak valid')
elif bangun_datar == 'Persegi Panjang':
    if hitung == 'Luas':
        luas = luas_persegi_panjang()
        print(luas)
    elif hitung == 'Keliling':
        keliling = keliling_persegi_panjang()
        print(keliling)
    else:
        print('Input tidak valid')
elif bangun_datar == 'Segitiga':
    if hitung == 'Luas':
        luas= luas_segitiga()
        print(luas)
    elif hitung == 'Keliling':
        keliling = keliling_segitiga()
        print(keliling)
    else:
        print('Input tidak valid')
else:
    print('Input tidak valid')