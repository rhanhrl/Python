
# Contoh generik dari format string

masukan = "Herlambang"
masukan2 = f"Raihan {masukan}"
print(masukan2)

masukan3 = "Assalamualaikum"
masukan4 = f"Halo {masukan3}"
print(masukan4)

masukan5 = True
masukan6 = f"Nilai bool adalah {masukan5}"
print(masukan6)

inputan = 2000
inputan2 = f"Bilangan {inputan:d}"
print(inputan2)

inputan3 = 1500000
inputan4 = f"Bilangan {inputan3:,}"
print(inputan4)

inputan5 = 123.1301
inputan6 = f"Bilangan {inputan5:.2f}"
print(inputan6)

inputan7 = 10021.2112
inputan8 = f"Bilangan {inputan7:010.2f}"
print(inputan8)

inputan9 = 100
inputan10 = -121
inputan11 = f"Bilangan {inputan9:+d}"
inputan12 = f"Bilangan {inputan10:+}"
print(inputan11)
print(inputan12)

inputan13 = 200
inputan14 = f"Bilangan {inputan13:%}"
print(inputan14)

inputan15 = 50
inputan16 = 60
inputan17 = f"Hasilnya {inputan15*inputan16:,}"
print(inputan17)

inputan18 = 672
inputan19 = f"Biner {bin(inputan18)}"
inputan20 = f"Oktal {oct(inputan18)}"
inputan21 = f"Hexa {hex(inputan18)}"
print(inputan19)
print(inputan20)
print(inputan21)

print('\r')

print(10*'>' + " " + 10*'<')
