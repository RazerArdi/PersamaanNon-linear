# Inisialisasi variabel
x, y, z = 0.05, 0.05, 0.05  # Tebakan awal
n_iterasi = 100  # Jumlah maksimum iterasi
toleransi_x = 1.2  # Toleransi untuk x
toleransi_y = 0.5  # Toleransi untuk y
toleransi_z = 0.5  # Toleransi untuk z

# Iterasi
for i in range(1, n_iterasi + 1):
    x_baru = (0.6 - 0.1*y + 0.3*z) / 0.4
    y_baru = (0.7 - 0.3*x + 0.2*z) / 0.5
    z_baru = (0.8 - 0.2*x + 0.3*y) / 0.4

    print(f'Iterasi {i}:')

    print(f'Dari persamaan pertama, kita hitung nilai x^({i}):')
    print(f'x^({i}) = (0.6 - 0.1*{y} + 0.3*{z}) / 0.4 = {x_baru:.5f}')

    print(f'Dari persamaan kedua, kita hitung nilai y^({i}):')
    print(f'y^({i}) = (0.7 - 0.3*{x} + 0.2*{z}) / 0.5 = {y_baru:.5f}')

    print(f'Dari persamaan ketiga, kita hitung nilai z^({i}):')
    print(f'z^({i}) = (0.8 - 0.2*{x} + 0.3*{y}) / 0.4 = {z_baru:.5f}\n')

    # Cek toleransi
    galat_x = abs(x_baru - x)
    galat_y = abs(y_baru - y)
    galat_z = abs(z_baru - z)

    print(f'Galat x = {galat_x:.5f}, didapat dari (penghitungan {x_baru:.5f} - {x:.5f})')
    print(f'Galat y = {galat_y:.5f}, didapat dari (penghitungan {y_baru:.5f} - {y:.5f})')
    print(f'Galat z = {galat_z:.5f}, didapat dari (penghitungan {z_baru:.5f} - {z:.5f})\n')

    if galat_x < toleransi_x and galat_y < toleransi_y and galat_z < toleransi_z:
        print(f'Iterasi berhenti pada iterasi ke-{i} karena galat x, y, dan z lebih kecil dari toleransi.')
        break

    x, y, z = x_baru, y_baru, z_baru

# Kesimpulan
if i == n_iterasi or (galat_x < toleransi_x and galat_y < toleransi_y and galat_z < toleransi_z):
    print(f'Kesimpulan:')
    print(f'Hasil akhir (x, y, z) pada iterasi terakhir:')
    print(f'x = {x:.5f}, y = {y:.5f}, z = {z:.5f}')
