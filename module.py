# membuat module

from module2 import tambah, kali, bagi
from module2 import kurang as minus

hasil_tambah = tambah(1,2,3)
print(f'hasil tambah = {hasil_tambah}')

hasil_kurang = minus(2)
print(f'hasil kurang = {hasil_kurang}')

hasil_kali = kali(3)
print(f'hasil kali = {hasil_kali}')

hasil_bagi = bagi(3)
print(f'hasil bagi = {hasil_bagi}')