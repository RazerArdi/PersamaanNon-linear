import math

# (1) Definisikan fungsi F(x)
def F(x):
    # Ubah basis logaritma (misalnya, basis 10)
    return math.log(x, b)

# (2) Tentukan nilai awal, error, dan iterasi maksimum
x0 = 1.15
epsilon = 0.11
n = 100
b = 10

# Output header
print("Hitunglah akar dari fungsi berikut dengan menggunakan metode Newton Raphson dengan:")
print(f"- Tebakan awal = {x0:.5f}")
print(f"- Error = {epsilon:.5f}\n")

x0_sebelum = x0  # Variabel untuk menyimpan x0 sebelumnya

for i in range(n + 1):
    # (3) Hitung F(x) dan F'(x)
    fx = F(x0)
    fpx = 1 / (x0 * math.log(b))  # Turunan dari log_b(x) adalah 1 / (x * ln(b))

    # Output iterasi
    print(f'Iterasi {i}:')
    print(f'xr = {x0:.5f} (didapat dari iterasi sebelumnya: x{i - 1} = {x0_sebelum:.5f} + dx = {x0:.5f})')
    print(f'f(xr){i + 1} = {fx:.5f} (nilai {fx:.5f} diperoleh dari F(x) = log_{b}({x0:.5f}))')
    print(f'f\'(xr){i + 1} = {fpx:.5f} (nilai {fpx:.5f} diperoleh dari turunan log_{b}(x))\n')

    # (4) Hitung x_i+1 menggunakan rumus metode Newton-Raphson
    x1 = x0 - fx / fpx

    # (5) Hitung selisih antara x1 dan x0
    selisih = abs(x1 - x0)

    if i >= 0:
        selisih_sebelum = abs(x1 - x0_sebelum)
        print("===============================================================================================================")
        print(f'|xr + 1 - xr{i + 1}| = {selisih:.6f} (nilai {selisih:.6f} diperoleh dari xr{i} = {x1:.5f} - xr{i - 1} = {x0:.5f})')
        print(f'perlu diketahui bahwa |xr + 1 - xr0| iterasi itu berada di iterasi selanjutnya. '
              f'contoh iterasi 0 adalah nilai |xr + 1 - xr0| dari iterasi 1\n')

        fx1 = F(x1)  # Hitung nilai F(x) pada x1
        fpx1 = 1 / (x1 * math.log(b))  # Hitung nilai F'(x) pada x1
        print(f'Iterasi {i + 1}:')
        print(f'xr = {x1:.5f} (didapat dari iterasi sebelumnya: x{i + 1} = {x0:.5f} - {fx:.5f}/{fpx:.5f} = {x1:.5f})')
        print(f'f(xr){i + 1} = {fx1:.5f} (nilai {fx1:.5f} diperoleh dari F(x) = log_{b}({x1:.5f})')
        print(f'f\'(xr){i + 1} = {fpx1:.5f} (nilai {fpx1:.5f} diperoleh dari turunan log_{b}(x1))\n')

    # (6) Periksa apakah |f(xi+1)| <= epsilon
    if abs(selisih) <= epsilon:
        print(f'Akar ditemukan di iterasi ke-{i + 1}. Akar persamaan: x = {x1:.5f} karena {selisih:.5f} <= {epsilon:.5f}\n')
        break

    # Update x0 dengan x1
    x0_sebelum = x0
    x0 = x1

if i == n and abs(selisih) > epsilon:
    print("Metode Newton-Raphson tidak konvergen setelah", n, "iterasi")
