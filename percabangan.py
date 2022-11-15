
masukan1 = int(input("Masukan angka 1 = "))
operator = input("Masukan operator = ")
masukan2 = int(input("Masukan angka 2 = "))

if operator == "+":
    hasil = masukan1 + masukan2
    print(f'Hasilnya adalah {hasil}')
elif operator == "-":
    hasil = masukan1 - masukan2
    print(f'Hasilnya adalah {hasil}')
elif operator == "x" or operator == "*":
    hasil = masukan1 * masukan2
    print(f'Hasilnya adalah {hasil}')
elif operator == "/":
    hasil = masukan1 // masukan2
    print(f'Hasilnya adalah {hasil}')
elif operator == ">":
    hasil = masukan1 > masukan2
    print(f'Hasilnya adalah {hasil}')
elif operator == "<":
    hasil = masukan1 < masukan2
    print(f'Hasilnya adalah {hasil}')
elif operator == "%":
    hasil = masukan1 % masukan2
    print(f'Hasilnya adalah {hasil}')
elif operator == "**":
    hasil = masukan1 ** masukan2
    print(f'Hasilnya adalah {hasil}')
else :
    print("Masukan salah !!!")

print()