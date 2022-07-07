# Operator dalam bentuk methods

# Merubah case dari string 

# Upper Case

sapaan = "Hai !"
print('Normal = ' + sapaan)

sapaan = sapaan.upper()
print('Upper  =', sapaan)

sapaan = sapaan.lower()
print('Lower  =', sapaan)

print('\n')
# Alokasi Karakter
penanda1 = "is method".rjust(15)
print(">" + penanda1 + "<")

penanda2 = "is method".ljust(15)
print(">" + penanda2 + "<")

penanda3 = "is method".center(15)
print(">" + penanda3 + "<")

penanda4 = "is method".strip()
print(penanda4)

print()
# Pengecekan is Case
sapaan1 = "halo"
apakah_upper = sapaan1.isupper()
print('Pengecekan is upper -> ' + sapaan1 + " adalah " 
+ str(apakah_upper))

apakah_lower = sapaan1.islower()
print('Pengecekan is lower -> ' + sapaan1 + " adalah " 
+ str(apakah_lower))

# isalpha() adalah untuk mengecek semua huruf
# isalnum() mengecek huruf dan angka
# isdecimal() angka
# isspace() spasi, tab, newline, \n
# istitle() semua kata dengan awalan huruf besar


sapaan2 = "hola"
test_alpha = sapaan2.isalpha()
print('Pengecekan is alpha -> ' + sapaan2 + " adalah " 
+ str(test_alpha))

test_alnum = sapaan2.isalnum()
print('Pengecekan is alnum -> ' + sapaan2 + " adalah "
+ str(test_alnum))

sapaan3 = "157"
test_decimal = sapaan3.isdecimal()
print('Pengecekan is decimal -> ' + sapaan3 + " adalah " 
+ str(test_decimal))
test_numeric = sapaan3.isnumeric()
print('Pengecekan is numeric -> ' + sapaan3 + " adalah " 
+ str(test_numeric))

test_space = sapaan3.isspace()
print('Pengecekan is space -> ' + sapaan3 + " adalah " 
+ str(test_space))

judul = "The Dragon"
test_title = judul.istitle()
print('Pengecekan is title -> ' + judul + " adalah "
+ str(test_title))

print('\r')

# Pengecekan dengan startswith dan endswith

startend = "suatu proposisi"
cek_start = startend.startswith("suatu")
print('''
Pengecekan startswith \-> 
''' + str(cek_start))

cek_end = startend.endswith("proposisi")
print('''
Pengecekan endswith \->
''' + str(cek_end))

# Penggabungan
print('\n')

data = ['Koefisien', 'Variabel', 'Konstanta']
print(data)

penggabungan = " , ".join(data)

penggabungan2 = " ".join(data)


print(
    penggabungan
)

print(
    penggabungan2
)

print(
    penggabungan2.split('Koefisien')
)

print('\r')
print(10*'>' + "------" + 10*'<')