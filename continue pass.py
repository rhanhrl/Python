# pass berfungsi sebagai dummy


angka = 0

while angka < 5:
    angka += 1
    

    if angka == 3:
        pass
    print(angka)

print(f'Akhir dari program')

# continue berfungsi seperti perintah skip

angka2 = 1

while angka2 < 10:
    angka2 +=1

    if angka2 == 2:
        continue
    print(f'Whassup')
print(f'Akhir program')