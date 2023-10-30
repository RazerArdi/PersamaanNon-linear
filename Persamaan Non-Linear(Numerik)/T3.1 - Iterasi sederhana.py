import math

# Fungsi iterasi g(x)
def g(x):
    return -0.5 * math.exp(x)

# Tebakan awal
x0 = -0.022

# Toleransi
epsilon = 0.001

# Inisialisasi iterasi
iterasi = 0

# Melakukan iterasi sampai mencapai toleransi
while True:
    iterasi += 1
    x1 = g(x0)  # Hitung nilai berikutnya dengan fungsi iterasi

    # Hitung selisih antara x1 dan x0
    selisih = abs(x1 - x0)

    # Output detail pengerjaan
    print(f'Iterasi {iterasi}:')
    print(f'xr = {g(x0):.5f} (didapat dari penghitungan berikut: -0.5 * e^({x0:.5f})) = {x1:.5f}')
    print(f'selisih = {x1:.5f} (didapat dari penghitungan berikut: -0.5 * e^({x0:.5f})) - {x0:.5f} (didapat dari penghitungan berikut: {x0:.5f}) = {selisih:.5f}\n')

    if selisih < epsilon:
        break

    x0 = x1  # Update x0 dengan x1

print(f'Akar persamaan: x = {x1:.5f}')


