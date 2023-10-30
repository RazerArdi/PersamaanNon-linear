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

# Membuat tabel
print("iterasi   Xr       Selisih")

# Melakukan iterasi sampai mencapai toleransi
while True:
    iterasi += 1
    x1 = g(x0)  # Hitung nilai berikutnya dengan fungsi iterasi

    # Hitung selisih antara x1 dan x0
    selisih = abs(x1 - x0)

    # Output iterasi dan tabel
    print(f"{iterasi}\t{x1:.5f}\t{selisih:.5f}")

    if selisih < epsilon:
        break

    x0 = x1  # Update x0 dengan x1

# Output akar persamaan
print(f'\nAkar persamaan: x = {x1:.5f}')
