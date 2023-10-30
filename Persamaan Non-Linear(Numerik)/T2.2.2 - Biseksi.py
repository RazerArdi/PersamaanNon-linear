import math

# Definisikan fungsi f(x)
def f(x):
    return x + math.exp(x)

# Nilai awal a dan b
a = -0.8
b = 0

# Toleransi (error) yang diinginkan
toleransi = 0.25

# Maksimal iterasi yang diizinkan
maksimal_iterasi = 100

# Inisialisasi iterasi
iterasi = 0

print("Iterasi\t  a\t\t   b\t\t   x\t\t   f(x)\t\t   f(a)\t\t   f(b)\t\t   Keterangan")
print("--------------------------------------------------------------------------------")

while iterasi < maksimal_iterasi:
    # Hitung nilai fungsi f(a) dan f(b)
    fa = f(a)
    fb = f(b)

    # Hitung nilai tengah x
    x = (a + b) / 2
    fx = f(x)

    # Tentukan apakah berlawanan tanda
    berlawanan_tanda = fa * fx < 0
    keterangan = "berlawanan tanda" if berlawanan_tanda else "tidak berlawanan tanda"

    # Tampilkan hasil iterasi
    print(f"{iterasi + 1}\t  {a:.5f}\t   {b:.5f}\t   {x:.5f}\t   {fx:.5f}\t   {fa:.5f}\t   {fb:.5f}\t   {keterangan}")

    # Periksa apakah toleransi terpenuhi
    if abs(fx) < toleransi:
        print("\nToleransi terpenuhi.")
        break

    # Update nilai a atau b berdasarkan berlawanan tanda
    if berlawanan_tanda:
        if fa * fx < 0:
            b = x
        else:
            a = x

    iterasi += 1
else:
    print("\nMaksimum iterasi tercapai. Akar tidak ditemukan.")

# Tampilkan hasil akhir
print(f"\nHasil akhir: x = {x:.5f}, f(x) = {fx:.5f}")
