# membuat tabel
from prettytable import PrettyTable

table = PrettyTable(["No", "Keinginan", "Hobi", "Cita - cita", "Quote"])
table.add_row(["1.", "Mewujudkan impian saya", "Sepak Bola", "Developer web", "Ubah lelah menjadi lillah"])
table.add_row(["2.", "Membahagiakan orang tua", "Ikan hias", "Pegawai negeri", "Hemat berat, tapi harus"])
table.add_row(["3.", "Membahagiakan keluarga", "Tanaman hias", "Pegawai bank", "Hidup itu mudah, yang sulit itu pikiranmu"])
table.add_row(["4.", "Membantu orang sekitar", "Kuliner", "Konsultan", "Bersyukur adalah makna"])
table.add_row(["5.", "Bermanfaat bagi orang lain", "Travelling", "Dosen", "Jalin kisah, jalin kasih"])

print(table)