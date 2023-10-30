import matplotlib.pyplot as plt

# Data Industri
total_industri = 1000
industri_primer = 300
industri_sekunder = 400
industri_tersier = 300

# Label sektor
labels = 'Industri Primer', 'Industri Sekunder', 'Industri Tersier'

# Persentase masing-masing sektor
sizes = [industri_primer, industri_sekunder, industri_tersier]

# Warna sektor
colors = ['red', 'green', 'blue']

# Pemecahan sektor Industri Primer
explode = (0.1, 0, 0)

# Membuat pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

# Judul
plt.title("Persentase Jumlah Industri")

# Menampilkan pie chart
plt.show()
