# Konversi dalam satuan temperature
# Temperature terdiri dari : Celcius, Reamur, Fahrenheit, Kelvin

# Konversi celcius ke satuan lain
print("---\PROGRAM CELCIUS/---")
celcius = float(input("masukan suhu dalam celcius ="))
print("suhu adalah =", celcius, "celcius")

# Reamur
reamur = (4/5) * celcius
print("suhu celcius dalam reamur =", reamur, "reamur")

# Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu celcius dalam fahrenheit =", fahrenheit, "fahrenheit")

# Kelvin
kelvin = celcius * 273
print("suhu celcius dalam kelvin =", kelvin, "kelvin")

print("~~~~~~~~")

# Konversi reamur ke satuan lain
print("---\PROGRAM REAMUR/---")
reamur = float(input("masukan suhu dalam reamur ="))
print("suhu adalah =", reamur, "reamur")

# Celcius
celcius = (5/4) * reamur
print("suhu reamur dalam celcius =", celcius, "celcius")

# Fahrenheit
fahrenheit = ((9/4) * reamur) + 32
print("suhu reamur dalam fahrenheit =", fahrenheit, "fahrenheit")

# Kelvin
kelvin = ((5/4) * reamur) + 273
print("suhu reamur dalam kelvin =", kelvin, "kelvin")

print("~~~~~~~~")

# Konversi fahrenheit ke satuan lain
print("---\PROGRAM FAHRENHEIT/---")
fahrenheit = float(input("Masukan suhu dalam fahrenheit ="))
print("suhu adalah =", fahrenheit, "fahrenheit")

# Celcius
celcius = 5/9 * (fahrenheit - 32)
print("suhu fahrenheit dalam celcius =", celcius, "celcius")

# Reamur
reamur = 4/9 * (fahrenheit - 32)
print("suhu fahrenheit dalam reamur =", reamur, "reamur")

# Kelvin
kelvin = (fahrenheit + 459.67) * 5/9
print("suhu fahrenheit dalam kelvin =", kelvin, "kelvin")

print("~~~~~~~~")

# Konversi kelvin ke satuan lain
print("---\PROGRAM KELVIN/---")
kelvin = float(input("masukan suhu dalam kelvin ="))
print("suhu adalah =", kelvin, "kelvin")

# Celcius
celcius = kelvin - 273
print("suhu kelvin dalam celcius =", celcius, "celcius")

# Reamur
reamur = 4/5 * (kelvin - 273)
print("suhu kelvin dalam reamur =", reamur, "reamur")

# Fahrenheit
fahrenheit = 9/5 * (kelvin -273) + 32
print("suhu kelvin dalam fahrenheit =", fahrenheit, "fahrenheit")

print("~~~~~~~~")