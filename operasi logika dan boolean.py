# Operasi Logika Dan Boolean


print('>>>> OPERASI LOGIKA DAN BOOLEAN <<<<')

# AND (Dimana ketika true dan true hasilnya true, yang lain false)
print('-------AND--------')
masukan1 = True 
masukan2 = True 
masukan3 = masukan1 and masukan2
print(masukan1, 'AND', masukan2, '=', masukan3)

print('---------------')
masukan4 = True
masukan5 = False
masukan6 = masukan4 and masukan5
print(masukan4, 'AND', masukan5, '=', masukan6)

print('---------------')
masukan7 = False
masukan8 = True
masukan9 = masukan7 and masukan8
print(masukan7, 'AND', masukan8, '=', masukan9)

print('---------------')
masukan10 = False
masukan11 = False
masukan12 = masukan10 and masukan11
print(masukan10, 'AND', masukan11, '=', masukan12)
print('===============')

# OR (Dimana ketika false dan false hasilnya false, yang lain true)
print('---------OR---------')
inputan1 = True
inputan2 = True
inputan3 = inputan1 or inputan2
print(inputan1, 'OR', inputan2, '=', inputan3)

print('---------------')
inputan3 = True
inputan4 = False
inputan5 = inputan3 or inputan4
print(inputan3, 'OR', inputan4, '=', inputan5)

print('---------------')
inputan6 = False
inputan7 = True
inputan8 = inputan6 or inputan7
print(inputan6, 'OR', inputan7, '=', inputan8)

print('---------------')
inputan9 = False
inputan10 = False
inputan11 = inputan9 or inputan10
print(inputan9, 'OR', inputan10, '=', inputan11)
print('===============')

# NOT (negasi atau kebalikannya)
print('--------NOT----------')
pertama = True
kedua = not pertama
print(pertama, 'NOT', '=', kedua)

print('----------------')
ketiga = False
keempat = not ketiga
print(ketiga, 'NOT', '=', keempat)
print('===============')

# XOR (Adalah apabila ada perbedaan maka hasilnya True, persamaan hasilnya False)
print('---------XOR----------')
data_satu = True
data_dua = True
data_tiga = data_satu ^ data_dua
print(data_satu, 'XOR', data_dua, '=', data_tiga)

print('----------------')
data_ketiga = True
data_keempat = False
data_kelima = data_ketiga ^ data_keempat
print(data_ketiga, 'XOR', data_keempat, '=', data_kelima)

print('----------------')
data_keenam = False
data_ketujuh = True
data_kedelapan = data_keenam ^ data_ketujuh
print(data_keenam, 'XOR', data_ketujuh, '=', data_kedelapan)

print('----------------')
data_kesembilan = False
data_kesepuluh = False
data_kesebelas = data_kesembilan ^ data_kesepuluh
data_keduabelas = not data_kesebelas
print(data_kesembilan, 'XOR', data_kesepuluh, '=', data_kesebelas)
print('===============')