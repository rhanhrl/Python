# membuat package dengan membuat folder berisikan file

import time
t_start = time.time()

import package.math

hasil_tambah = package.math.tambah(1,2,3,4)
print(f'hasil tambah = {hasil_tambah}\n')

hasil_kurang = package.math.kurang(5)
print(f'hasil kurang = {hasil_kurang}\n')

hasil_kali = package.math.kali(2)
print(f'hasil kali = {hasil_kali}\n')

hasil_bagi = package.math.bagi(4)
print(f'hasil bagi = {hasil_bagi}\n')

t_end = time.time()
print(f'waktu eksekusi {t_start - t_end}')
