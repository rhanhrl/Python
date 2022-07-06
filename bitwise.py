# OR

print('========OR========')

inputan1 = 17
inputan2 = 12
inputan3 = inputan1 | inputan2

print('-------------------------------------------------------')
print('nilai :', inputan1, 'binary :', format(inputan1, '08b'))
print('nilai :', inputan2, 'binary :', format(inputan2, '08b'))
print('-------------------------------------------------------')
print('nilai :', inputan3, 'binary :', format(inputan3, '08b'))


# AND

print('========AND========')

masukan1 = 20
masukan2 = 21
masukan3 = masukan1 & masukan2

print('------------------------------------------------------')
print('nilai :', masukan1, 'binary :', format(masukan1, '08b'))
print('nilai :', masukan2, 'binary :', format(masukan2, '08b'))
print('-------------------------------------------------------')
print('nilai :', masukan3, 'binary :', format(masukan3, '08b'))


# XOR 

print('========XOR========')

koefisien_a = 31
koefisien_b = 23
koefisien_c = koefisien_a ^ koefisien_b

print('------------------------------------------------------')
print('nilai :', koefisien_a, 'binary :', format(koefisien_a, '08b'))
print('nilai :', koefisien_b, 'binary :', format(koefisien_b, '08b'))
print('------------------------------------------------------')
print('nilai :', koefisien_c, 'binary :', format(koefisien_c, '08b'))


# Negasi

print('========NOT========')

negasi = (~ koefisien_a)


print('------------------------------------------------------')
print('nilai negasi dari keofisien a :', negasi, 'binary :', format(negasi, '08b'))


# Shifting

print('========SHIFTING========')

konstanta_a = koefisien_a > 1


print('------------------------------------------------------')
print('nilai :', konstanta_a, 'binary :', format(konstanta_a, '08b'))
print('======================================================')