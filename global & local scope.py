# global dan local scope python

nama = "raihan" #<- variabel global

# akses variabel dalam fungsi
def fungsi():
    "global scope dalam fungsi"
    print(f"Nama saya {nama}")
fungsi()

# akses variabel dalam loop
for i in range(0,5):
    "global scope dalam loop"
    print(f"loop{i} - {nama}\n")


# akses variabel dalam percabangan
if True:
    print(f"menampilkan variabel global {nama}\n")

# variabel local scope
def fungsi2():
    "local scope dalam fungsi"
    nama = "raihan"#tidak bisa diakses diluar fungsi
fungsi()
#print(nama)

#contoh 1
def say():
    print(f"hello {nama2}")
nama2 = "herlambang"
say()

# contoh 2
nama3 = "raihan"
umur = 20
def nilai(name, age):
    global nama3
    global umur
    nama3 = name
    umur = age
print(f"sebelum {nama3, umur}")
nilai("herlambang", 19)
print(f"sesudah {nama3, umur}")

# contoh 3
angka = 0

for i in range(0,5):
    angka += i
    angkalain = 0
print(angka)
print(angkalain)

if True:
    angka = 10
    angkalain = 10
print(angka)
print(angkalain)