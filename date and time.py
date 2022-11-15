import datetime as dt

print('Slahkan isi tanggal, bulan, tahun lahir anda')

tgl = int(input('>\tTanggal lahir \t\t: '))
bln = int(input('>\tBulan lahir   \t\t: '))
thn = int(input('>\tTahun lahir   \t\t: '))

print(
    '\r'
)

print(f'Data lahir anda\n{tgl} adalah tanggal lahir \n{bln} adalah bulan lahir \n{thn} adalah tahun lahir')

datalahir = dt.date(thn,bln,tgl)

print(datalahir)

print(
    '\r'
)

datacal = dt.date.today()
print(datacal)

umur = datacal - datalahir
umurtahun = umur.days // 365
umurbulan = (umur.days % 365) // 30

print(f'Umur anda adalah \n{umurtahun} tahun\n{umurbulan} bulan')

print(
    '\r'
)

print(f'Hari lahir {datalahir:%A}')
print(f'Bulan lahir {datalahir:%B}')
print(f'Tahun lahir {datalahir:%G}')

print(
    '\r'
)

import calendar
cal = calendar.month(2002, 12)
print(cal)