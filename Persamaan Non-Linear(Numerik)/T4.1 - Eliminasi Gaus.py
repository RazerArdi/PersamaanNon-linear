import numpy as np

# Input ordo matriks
n = int(input("Tentukan ordo matriks: "))

# Input matriks A
A = np.zeros((n, n))
print("Masukkan matriks A:")
for i in range(n):
    for j in range(n):
        A[i][j] = float(input(f"Matriks A[{i+1}][{j+1}]: "))

# Input vektor B
B = np.zeros(n)
print("Masukkan vektor B:")
for i in range(n):
    B[i] = float(input(f"Vektor B[{i+1}]: "))

# Buat augmented matriks [A|B]
AB = np.column_stack((A, B))

# Output matriks awal
print("Matriks Awal [A|B]:")
print(AB)

# Operasi eliminasi Gauss
for i in range(n):
    if AB[i][i] == 0:
        for k in range(i + 1, n):
            if AB[k][i] != 0:
                AB[[i, k]] = AB[[k, i]]
                break
        else:
            print("Perhitungan tidak dapat dilanjutkan. Matriks singular.")
            exit(1)
    AB[i] = AB[i] / AB[i][i]
    for j in range(i + 1, n):
        factor = AB[j][i]
        AB[j] -= factor * AB[i]

# Output matriks setelah OBE
print("Matriks setelah OBE:")
for i in range(n):
    print(f"Baris {i + 1}:")
    for j in range(n):
        print(f"A[{i+1}][{j+1}] = {AB[i][j]:.4f}, didapat dari eliminasi Gauss")
    print(f"B[{i+1}] = {AB[i][n]:.4f}, didapat dari eliminasi Gauss")
    print()

# Hitung solusi x
x = np.zeros(n)
x[n - 1] = AB[n - 1][n]
for i in range(n - 2, -1, -1):
    x[i] = AB[i][n] - np.sum(AB[i, i + 1:n] * x[i + 1:])

# Cetak solusi persamaan simultan
print("Penyelesaian persamaan simultan:")
for i in range(n):
    print(f"x{i+1} = {x[i]:.4f}")
