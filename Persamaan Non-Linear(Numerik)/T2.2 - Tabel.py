import math

# Definisikan fungsi f(x)
def fx(x):
    return x + math.exp(x)

# Tentukan batas bawah (X_bawah) dan batas atas (X_atas) dari rentang
X_bawah = -1
X_atas = 0

# Tentukan jumlah pembagian (N)
N = 10

# Hitung step pembagi (h)
h = (X_atas - X_bawah) / N

# Inisialisasi tabel untuk nilai X dan f(X)
table = []

# Iterasi untuk menghitung nilai f(X) dalam rentang
for i in range(N + 1):
    X = X_bawah + i * h
    f_X = fx(X)
    table.append((X, f_X))

# Menampilkan tabel hasil
print("No\t    x\t\t   f(x)")
for i, (X, f_X) in enumerate(table):
    print(f"{i+1}\t{X:.6f}\t{f_X:.6f}")

# Mencari akar dengan metode iteratif
akar_ditemukan = False
for i in range(N):
    X1, f_X1 = table[i]
    X2, f_X2 = table[i + 1]

    if f_X1 * f_X2 < 0:
        if abs(f_X1) < abs(f_X2):
            akar = X1
        else:
            akar = X2
        akar_ditemukan = True
        break

if akar_ditemukan:
    print(f"\nAkar ditemukan pada x = {akar:.6f}")
else:
    print("\nTidak ada akar yang ditemukan dalam rentang yang diberikan.")
