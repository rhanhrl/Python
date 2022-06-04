# data integer atau satuan angka
data_integer = 1
print("data :", data_integer)
print("data ini termasuk tipe :", type(data_integer))

# data float atau angka dengan koma
data_float = 6.7
print("data :", data_float)
print("data ini termasuk tipe :", type(data_float))

# data string atau satuan karakter
data_string = "raihan"
print("data :", data_string)
print("data ini termasuk tipe :", type(data_string))

#data boolean atau (biner) true / false
data_bool = True
print("data :", data_bool)
print("data ini termasuk :", type(data_bool))

# data complex atau bilangan kompleks
data_complex = complex (10,7)
print("data :", data_complex)
print("data ini termasuk tipe :", type(data_complex))

# data dari bahasa c
from ctypes import c_double
data_c_double = c_double (20.7)
print("data :", data_c_double)
print("data ini termasuk tipe :", type(c_double))