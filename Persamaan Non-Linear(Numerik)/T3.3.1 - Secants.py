import math

def f(x):
    return math.exp(x) + math.exp(x) - 2

error = 0.5
x0 = 1
x1 = 2
iterasi = 0

header = "{:<10} {:<14} {:<14} {:<14} {:<14} {:<14} {:<14} {:<10}".format(
    "Iterasi", "x_i-1", "x_i", "x_i+1", "f(x_i-1)", "f(x_i)", "f(x_i+1)", "Error")
separator = "=" * len(header)

print(header)
print(separator)

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

    # Mencetak baris tabel dengan format yang rapi
    row = "{:<10} {:<14.6f} {:<14.6f} {:<14.6f} {:<14.6f} {:<14.6f} {:<14.6f} {:<10.6f}".format(
        iterasi, x0, x1, x2, y0, y1, y2, delta_x)
    print(row)

    # Akar ditemukan jika error kurang dari toleransi
    if delta_x < error:
        print(f"\nAkar fungsi ditemukan di iterasi ke-{iterasi}. Akar persamaan: x = {x1:.6f}")
        break

    # Update x0, x1, dan x2 untuk iterasi berikutnya
    x0 = x1
    x1 = x2
