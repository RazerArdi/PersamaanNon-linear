import math

# (1) Definisikan fungsi F(x) sesuai dengan f(x) yang baru
def F(x):
    return e + x**2 + 5*x

# (2) Tentukan nilai awal, error, dan iterasi maksimum
x0 = 12
epsilon = 5
n = 100
e = 2.71828

# Output header
print("Hitunglah akar dari fungsi berikut dengan menggunakan metode Newton Raphson dengan:")
print(f"- Tebakan awal = {x0:.5f}")
print(f"- Error = {epsilon:.5f}\n")

x0_sebelum = x0  # Variabel untuk menyimpan x0 sebelumnya

for i in range(n + 1):
    # (3) Hitung F(x) dan F'(x) sesuai dengan f(x) yang baru
    fx = F(x0)
    fpx = 2 * x0 + 5  # Turunan fungsi f(x)

    # Output iterasi
    print(f'Iterasi {i}:')
    print(f'xr = {x0:.5f} (didapat dari iterasi sebelumnya: x{i - 1} = {x0_sebelum:.5f} - dx = {x0:.5f})')
    print(f'f(xr){i} = {fx:.5f} (nilai {fx:.5f} diperoleh dari F(x) = e + x^2 + 5x)')
    print(f'f\'(xr){i} = {fpx:.5f} (nilai {fpx:.5f} diperoleh dari turunan f(x))\n')

    # (4) Hitung x_i+1 menggunakan rumus metode Newton-Raphson
    x1 = x0 - fx / fpx

    # (5) Hitung selisih antara x1 dan x0
    selisih = abs(x1 - x0)

    if i >= 0:
        selisih_sebelum = abs(x1 - x0_sebelum)
        print("===============================================================================================================")
        print(f'|xr{i + 1} - xr{i}| = {selisih:.6f} (nilai {selisih:.6f} diperoleh dari xr{i + 1} = {x1:.5f} - xr{i} = {x0:.5f})\n')

        fx1 = F(x1)  # Hitung nilai F(x) pada x1
        fpx1 = 2 * x1 + 5  # Hitung nilai F'(x) pada x1

        print(f'Iterasi {i + 1}:')
        print(f'xr = {x1:.5f} (didapat dari iterasi sebelumnya: x{i} = {x0:.5f} - {fx:.5f}/{fpx:.5f} = {x1:.5f})')
        print(f'f(xr){i + 1} = {fx1:.5f} (nilai {fx1:.5f} diperoleh dari F(x) = e + x^2 + 5x)')
        print(f'f\'(xr){i + 1} = {fpx1:.5f} (nilai {fpx1:.5f} diperoleh dari turunan f(x))\n')

    # (6) Periksa apakah |f(xi+1)| <= epsilon
    if abs(selisih) <= epsilon:
        print(f'Akar ditemukan di iterasi ke-{i + 1}. Akar persamaan: x = {x1:.5f} karena {selisih:.5f} <= {epsilon:.5f}\n')
        break

    # Update x0 dengan x1
    x0_sebelum = x0
    x0 = x1

if i == n and abs(selisih) > epsilon:
    print("Metode Newton-Raphson tidak konvergen setelah", n, "iterasi")
