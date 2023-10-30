import math

# (1) Definisikan fungsi f(x)
def f(x):
    return x * math.exp(-x) + 1

# (2) Tentukan batas bawah (a) dan batas atas (b)
a = -1.0
b = 0.0

# (3) Tentukan toleransi error (e) dan iterasi maksimum (n)
e = 0.001
n = 100

# Inisialisasi nilai awal
Fa = f(a)
Fb = f(b)

# Buat tabel untuk mencatat iterasi
print('Iterasi\t  a\t\t   b\t\t   Fa\t\t   Fb\t\t   x\t\t   Fx\t\t   Error')
print('-----------------------------------------------------------------------------')

for i in range(1, n + 1):
    # (4) Hitung x dengan rumus Regula Falsi
    x = (a * Fb - b * Fa) / (Fb - Fa)
    Fx = f(x)
    error = abs(Fx)

    # Tambahkan hasil iterasi ke tabel
    print(f'{i}\t  {a:.6f}\t   {b:.6f}\t   {Fa:.6f}\t   {Fb:.6f}\t   {x:.6f}\t   {Fx:.6f}\t   {error:.6f}')

    # (5) Periksa berhenti jika error lebih kecil dari e atau telah mencapai n iterasi
    if error < e:
        print(f'Akar ditemukan di iterasi ke-{i}. x = {x:.6f}')
        break
    elif Fa * Fx < 0:
        b = x
        Fb = Fx
    else:
        a = x
        Fa = Fx
else:
    print("Metode Regula Falsi tidak konvergen setelah", n, "iterasi")

# Bagian 6: Akar persamaan adalah x
akar = (a * Fb - b * Fa) / (Fb - Fa)
print(f'Akar persamaan: x = {akar:.6f}')
