import math


# (1) Definisikan fungsi f(x)
def f(x):
    return x + 12 * math.exp(-x) - 15


# (2) Tentukan batas bawah (a) dan batas atas (b)
a = 2
b = -1

# (3) Tentukan toleransi error (e) dan iterasi maksimum (n)
e = 0.52
n = 100

# Inisialisasi nilai awal
Fa = f(a)
Fb = f(b)

# Bagian 4: Hitung Fa dan Fb
Fa = f(a)
Fb = f(b)

for i in range(1, n + 1):
    # (5) Hitung Fx
    x = (Fb * a - Fa * b) / (Fb - Fa)
    Fx = f(x)
    error = abs(Fx)

    # Tambahkan hasil iterasi ke tabel
    print(f'Iterasi {i}\n')
    print(f'a = {a:.5f}, b = {b:.5f}')
    print(f'Fa = {Fa:.5f}, Fb = {Fb:.5f}')
    print(f'x = {x:.5f}, Fx = {Fx:.5f}')
    print(f'Error = {error:.5f}\n')
    print(f'a = {a:.5f}')
    print(f'b = {b:.5f}')
    print(f'F(a) = -e^-(-1)+1 = {Fa:.5f}')
    print(f'F(b) = e^-0+1 = {Fb:.5f}')
    print(f'F(x) = -{x:.5f}e^-({x:.5f})+1 = {Fx:.5f}')
    print(f'x = ({Fb:.5f} * {a:.5f} - {Fa:.5f} * {b:.5f}) / ({Fb:.5f} - {Fa:.5f} = {x:.5f})')

    Fa_times_Fx = Fa * Fx

    # Cek apakah Fa*Fx < 0 atau tidak
    if Fa_times_Fx < 0:
        b = x
        Fb = Fx
        print(f'Karena {Fx} x {Fa} {Fa_times_Fx:.5f} < 0, maka b = x dan Fb = Fx\n')
    else:
        a = x
        Fa = Fx
        print(f'Karena {Fa_times_Fx:.5f} >= 0, maka a = x dan Fa = Fx\n')

    # Periksa berhenti jika error lebih kecil dari e atau telah mencapai n iterasi
    if error < e:
        print(f'Akar ditemukan di iterasi ke-{i}. x = {x:.5f}\n')
        break
else:
    print("Metode biseksi tidak konvergen setelah", n, "iterasi")

# Bagian 6: Akar persamaan adalah x
akar = (a + b) / 2
print(f'Akar persamaan: x = {akar:.5f}')
