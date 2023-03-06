# lambda function

def fungsi(angka):
    return angka**2
print(f"2 pangkat 2 adalah {fungsi(2)}")

# contoh lambda
kuadrat = lambda angka : angka**2
print(f"3 pangkat 2 adalah {kuadrat(3)}")

kuadrat2 = lambda num, pow: num**pow
print(f"4 pangkat 2 adalah {kuadrat2(2,2)}\n")

# sorting list biasa

data = ["raihan", "herlambang"]
data.sort()
print(f"berdasarkan sorting data = {data}")
data.sort(key=len)
print(f"berdasarkan sorting data len = {data}\n")

# sorting menggunakan panjang
def nama(namadata):
    return len(namadata)
data.sort(key=nama)
print(f"menggunakan sorting panjang pada fungsi = {data}")
data.sort(key=lambda nama : len(nama))
print(f"menggunakan sorting panjang dengan lambda = {data}\n")

# filter
dataangka = [1,2,3,4,5,6,7,8,9,10]
def databaru(dataangkabaru):
    return dataangkabaru < 5
datalain = list(filter(databaru,dataangka))
datalain = list(filter(lambda x:x<8, dataangka))
print(datalain)

#kasus genap
datagenap = list(filter(lambda x:(x%2==0), dataangka))
print(datagenap)

#kasus ganjil
dataganjil = list(filter(lambda x:(x%2!=0), dataangka))
print(dataganjil)

#kelipatan 3 
datakelip = list(filter(lambda x:(x%3==0), dataangka))
print(datakelip)

# dengan currying
def pangkat(n):
    return lambda angka:angka**n
hasil = pangkat(2)
print(f"pangkat 2 dari 5 = {hasil(5)}")
hasil = pangkat(3)
print(f"pangkat 3 dari 6 = {hasil(6)}")