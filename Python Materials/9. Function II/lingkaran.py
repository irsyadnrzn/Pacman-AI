from math import pi

def luas_lingkaran():
    jari = float(input('Masukkan jari - jari lingkaran: '))
    luas = pi * jari * jari
    return luas 

def keliling_lingkaran():
    jari = float(input('Masukkan jari - jari lingkaran: '))
    keliling = 2 * pi * jari
    return keliling