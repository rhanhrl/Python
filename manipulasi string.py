# Manipulasi String

awalan = 'Aku'

nama_awal = 'Raihan'

nama_akhir = 'Herlambang'

nama_lengkap = awalan + " " + nama_awal + " " + nama_akhir

print(nama_lengkap)

# Menghitung String

ukuran = len(nama_lengkap)

print(ukuran)

print('Nama lengkap =' + " " + nama_lengkap + " " + '\nBerukuran =' + " " + str(ukuran))


print('------------------------------------------------')

# Mengecek String

pengecekan_1 = 'D' in nama_lengkap

print('Hasil Pengecekan', pengecekan_1)

pengecekan_2 = 'R' in nama_lengkap

print('Hasil Pengecekan', pengecekan_2)

pengecekan_3 = 'D' not in nama_lengkap

print('Hasil Pengecekan', pengecekan_3)

pengecekan_4 = 'R' not in nama_lengkap

print('Hasil Pengecekan', pengecekan_4)


print('------------------------------------------------')

# Mengulang String

a = 'awok'
b = 'akwk'
c = ('awkok'*2)
d = a + b + c

print(d)

print('------------------------------------------------')

# Indexing

print('Index ke 0 =', nama_lengkap[0])
print('Index ke 1 =', nama_lengkap[1])
print('Index ke 2 =', nama_lengkap[2])
print('Index ke 3 =', nama_lengkap[3])
print('Index ke 4 =', nama_lengkap[4])
print('Index ke 5 =', nama_lengkap[5])
print('Index ke 6 =', nama_lengkap[6])
print('Index ke 7 =', nama_lengkap[7])
print('Index ke 8 =', nama_lengkap[8])
print('Index ke 9 =', nama_lengkap[9])
print('Index ke 10 =', nama_lengkap[10])

print('Index ke 0 sampai 5 =', nama_lengkap[0:6])
print('Index ke 0, 2, 4, 6, 8, 10 = ', nama_lengkap[0:10:2])

print('------------------------------------------------')

# Menghitung Item

print('Paling kecilnya =' + " " + min(nama_lengkap))

print('Paling besarnya =' + " " + max(nama_lengkap))

Ascii_code = ord(" ")
print('Ascii code untuk spasi adalah =', str(Ascii_code))

Ascii_code1 = 213
print('Ascii code dari 213 adalah =', chr(Ascii_code1))

print('------------------------------------------------')