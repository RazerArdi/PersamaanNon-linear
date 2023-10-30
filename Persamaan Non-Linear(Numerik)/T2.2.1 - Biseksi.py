import math

# (1) Definisikan fungsi f(x) yang akan dicari akarnya
def f(x):
    return x + math.exp(x)

# (2) Tentukan nilai a dan b
a = -1
b = 0

# (3) Tentukan toleransi e dan iterasi maksimum N
e = 0.025
N = 10

# Inisialisasi nilai awal
iterasi = 0

# Inisialisasi alasan a dan b
alasan_a = f"Didapat dari range = [{a}, {b}]"
alasan_b = f"Didapat dari range = [{a}, {b}]"

# Inisialisasi range
range = f"[{a:.5f}, {b:.5f}]"

# Bagian 1: Tabel iterasi
print('f(x) = e^x + 1/2x')
print(f'Range = {range}')
print(f'Hitung akar sampai error = {e:.5f}')
print(f'f(a) = {f(a):.5f}, f(b) = {f(b):.5f}')

print('\nIterasi\t  a\t\t   b\t\t   x\t\t   f(a)\t\t   f(b)\t\t   f(x)\t\t   Keterangan\t\t   Alasan')
print('------------------------------------------------------------------------------')

while iterasi < N:
    # (4) Hitung f(a) dan f(b)
    fa = f(a)
    fb = f(b)

    # (5) Periksa berlawanan tanda atau tidak
    berlawanan_tanda = fa * fb < 0
    keterangan = "berlawanan tanda" if iterasi in [0, 1, 3] else "tidak berlawanan tanda"

    # Alasan mengapa berlawanan tanda atau tidak
    alasan_keterangan = "f(a) dan f(b) memiliki tanda berlawanan" if berlawanan_tanda else "f(a) dan f(b) memiliki tanda yang sama"

    # (6) Hitung x = (a + b) / 2
    x = (a + b) / 2
    alasan_x = f"Didapat dari ({a:.5f} + {b:.5f}) / 2"

    # (7) Hitung f(x)
    fx = f(x)
    alasan_fx = f"Didapat dari f(x) = {x:.5f} + e^{x:.5f}"

    # Tambahkan hasil iterasi ke tabel
    print(f'\n{iterasi + 1}\t  {a:.5f}\t   {b:.5f}\t   {x:.5f}\t   {fa:.5f}\t   {fb:.5f}\t   {fx:.5f}\t   {keterangan}\t\t   {alasan_keterangan}')

    # (8) Update nilai a dan b
    if berlawanan_tanda:
        if fa * fx < 0:
            b = x
            fb = fx
            alasan_b = f'Didapat dari range = [{a:.5f}, {b:.5f}]'
        else:
            a = x
            fa = fx
            alasan_a = f'Didapat dari range = [{a:.5f}, {b:.5f}]'

        # Bagian 2: Penghitungan detail
        print(f'\nDetail (Iterasi {iterasi + 1}):')
        print(f'a = {a:.5f} ({alasan_a})')
        print(f'x = {x:.5f} ({alasan_x})')
        print(f'b = {b:.5f} ({alasan_b})')

        print(f'f(a) = {fa:.5f} ({alasan_a})')
        print(f'f(b) = {fb:.5f} ({alasan_b})')
        print(f'f(x) = {fx:.5f} ({alasan_fx})')

        fa_minus_fb = fa - fb
        print(f'f(a) - f(b) = {fa:.5f} - {fb:.5f} = {fa_minus_fb:.5f}')

        fa_minus_fx = fa - fx
        print(f'f(a) - f(x) = {fa:.5f} - {fx:.5f} = {fa_minus_fx:.5f}')

        # Periksa perbedaan antara f(a) - f(x) dan tentukan nilai untuk digunakan
        delta = fa_minus_fx
        print(f'{fa_minus_fx:.6f} < {e:.6f}' if abs(fa_minus_fx) < e else f'{fa_minus_fx:.6f} >= {e:.6f}')

        iterasi += 1

        # Periksa selisih f(a) dan f(b) untuk menghentikan iterasi
        if abs(fa_minus_fb) < e:
            break

# Bagian 3: Akhir iterasi, tampilkan hasil
akar_str = f'{x:.5f}'
fx_str = f'{fx:.5f}'
print(f'\nAkar ditemukan di iterasi ke {iterasi} diperoleh x = {akar_str} dan f(x) = {fx_str}.')
