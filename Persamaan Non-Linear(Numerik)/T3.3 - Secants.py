import math

def f(x):
    return math.exp(x) + math.exp(x) - 2

# Toleransi error
error = 0.5

# Tebakan awal
x0 = 1
x1 = 2

# Inisialisasi iterasi
iterasi = 0

while True:
    iterasi += 1

    # Hitung nilai fungsi pada x0, x1, dan x2
    y0 = f(x0)
    y1 = f(x1)

    # Hitung x2 menggunakan metode Secant
    x2 = x1 - (y1 * (x1 - x0)) / (y1 - y0)
    y2 = f(x2)  # Hitung f(x) pada x2

    # Hitung error
    delta_x = abs(x1 - x0)

    print(f"Iterasi {iterasi}:")

    # Detail lengkap untuk x0
    rumus_x0 = f"x0 = {x0:.5f}"
    perhitungan_x0 = f"x0 = {x0:.5f} (Tebakan awal)"
    hasil_x0 = x0

    print(f"{rumus_x0} = (X_i-1) = {perhitungan_x0} = {hasil_x0:.5f} ")

    # Detail lengkap untuk x1
    rumus_x1 = f"x1 = {x1:.5f}"
    perhitungan_x1 = f"x1 = {x1:.5f} (Tebakan awal)"
    hasil_x1 = x1

    print(f"{rumus_x1} = (X_i) = {perhitungan_x1} = {hasil_x1:.5f} ")

    # Detail lengkap untuk x2
    rumus_x2 = f"x2 = x1 - (y1 * (x1 - x0)) / (y1 - y0)"
    perhitungan_x2 = f"x2 = {x1:.5f} - ({y1:.5f} * ({x1:.5f} - {x0:.5f})) / ({y1:.5f} - {y0:.5f})"
    hasil_x2 = x2

    print(f"{rumus_x2} = (X_i+1) = {perhitungan_x2} = {hasil_x2:.5f} ")

    # Detail lengkap untuk f(x0)
    rumus_fx0 = f"f(x0) = e^x - x"
    perhitungan_fx0 = f"f(x0) = e^{x0:.5f} - {x0:.5f}"
    hasil_fx0 = y0

    print(f"{rumus_fx0} = f(X_i-1) = {perhitungan_fx0} = {hasil_fx0:.5f} ")

    # Detail lengkap untuk f(x1)
    rumus_fx1 = f"f(x1) = e^x - x"
    perhitungan_fx1 = f"f(x1) = e^{x1:.5f} - {x1:.5f}"
    hasil_fx1 = y1

    print(f"{rumus_fx1} = f(X_i) = {perhitungan_fx1} = {hasil_fx1:.5f} ")

    # Detail lengkap untuk f(x2)
    rumus_fx2 = f"f(x2) = e^x - x"
    perhitungan_fx2 = f"f(x2) = e^{x2:.5f} - {x2:.5f}"
    hasil_fx2 = y2

    print(f"{rumus_fx2} = f(X_i+1) = {perhitungan_fx2} = {hasil_fx2:.5f} ")

    # Detail lengkap untuk delta_x
    rumus_delta_x = f"|x1 - x0|"
    perhitungan_delta_x = f"|{x1:.5f} - {x0:.5f}|"
    hasil_delta_x = delta_x

    print(f"{rumus_delta_x} = {perhitungan_delta_x} = {hasil_delta_x:.5f} (Error)\n")

    # Akar ditemukan jika error kurang dari toleransi
    if delta_x < error:
        print(f"Akar fungsi ditemukan di iterasi ke-{iterasi}. Akar persamaan: x = {x1:.5f}")
        break

    # Update x0, x1, dan x2 untuk iterasi berikutnya
    x0 = x1
    x1 = x2
