# Inisialisasi variabel
x, y, z = 1,2,2  # Tebakan awal
n_iterasi = 3
T1, T2, T3 = 2 , 4, 3

# Inisialisasi daftar untuk menyimpan galat di setiap iterasi
galat_x = []
galat_y = []
galat_z = []

print("Psulusi:")
print(f'x : {T1}\n'
      f'y : {T2}\n'
      f'z : {T3}\n')

print("Tebakan awal:")
print(f'x : {x}\n'
      f'y : {y}\n'
      f'z : {z}\n')

# Iterasi
for i in range(1, n_iterasi + 1):
    x_baru = (7 + y - z) / 2
    y_baru = (21 + 4 * x_baru + z) / 6
    z_baru = (15 + 2 * x_baru - y_baru) / 2


    galat_x.append(abs(x_baru - x))
    galat_y.append(abs(y_baru - y))
    galat_z.append(abs(z_baru - z))

    print(f'Iterasi {i}:')
    print(f'x_{i} = {x_baru:.5f} (Didapat dari X_{i} = (7 + y - z)/4 = {(7 + y - z)/4:.5f})')
    print(f'y_{i} = {y_baru:.5f} (Didapat dari Y_{i} = (21 + 4 * x_{i} + z)/8 = {(21 + 4 * x_baru + z)/8:.5f})')
    print(f'z_{i} = {z_baru:.5f} (Didapat dari Z_{i} = (15 + 2 * x_{i} - y_{i})/5 = {(15 + 2 * x_baru - y_baru)/5:.5f})')
    print(f'Galat/error iterasi {i} : |X| = | {T1} - {x_baru:.5f}|={T1 - x_baru:.5f}, |Y| = |{T2} - {y_baru:.5f}|={T2 - y_baru:.5f}, |Z| = |{T3} - {z_baru:.5f}|={T3 - z_baru:.5f}\n')

    x, y, z = x_baru, y_baru, z_baru

# Kesimpulan
if max(galat_x[-1], galat_y[-1], galat_z[-1]) < 0.001:
    print(f'Error ditemukan di iterasi ke {n_iterasi} karena galat sudah kurang dari 0.001.')
else:
    print(f'Error tidak ditemukan hingga iterasi ke {n_iterasi}.')

# Hasil akhir
print(f'Hasil akhir (x, y, z): ({x:.5f}, {y:.5f}, {z:.5f})')
