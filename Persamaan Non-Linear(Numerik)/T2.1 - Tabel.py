# (1) Definisikan fungsi f(x) yang akan dicari akarnya
import math


def f(x):
    return x + math.exp(x)


# (2) Tentukan nilai a dan b
a = -1
b = 0

# (3) Tentukan toleransi e dan iterasi maksimum N
e = 0.072
N = 100

# Inisialisasi iterasi
iterasi = 0

while iterasi < N:
    # (4) Hitung f(a) dan f(b)
    fa = f(a)
    fb = f(b)

    # (5) Periksa apakah f(a) * f(b) > 0
    if fa * fb > 0:
        print("Tidak ada akar karena f(a) * f(b) > 0")
        break

    # (6) Hitung x = (a + b) / 2
    x = (a + b) / 2

    # (7) Hitung f(x)
    fx = f(x)

    # (8) Update nilai a dan b
    if fa * fx < 0:
        b = x
        fb = fx
    else:
        a = x
        fa = fx

    # (9) Periksa apakah toleransi terpenuhi
    if abs(b - a) < e:
        break

    iterasi += 1

# Tampilkan hasil akhir
if iterasi < N:
    print("Akar ditemukan di iterasi ke", iterasi + 1)
    print("Akar =", x)
else:
    print("Akar tidak ditemukan dalam iterasi maksimum")
