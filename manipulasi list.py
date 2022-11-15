data = ['Raihan', 1, 'Herlambang', True]
print(f'data pertama adalah {data}')

# indexing

dataindex1 = data[0]
dataindex2 = data[1]
dataindex3 = data[2]
dataindex4 = data[3]

print(f'data index 1 = {dataindex1}')
print(f'data index 2 = {dataindex2}')
print(f'data index 3 = {dataindex3}')
print(f'data index 4 = {dataindex4}')

# menghitung jumlah 
datajumlah = len(data)
print(datajumlah)

# memasukan data 
data.insert(0, "Saya")
print(f'data sekarang adalah {data}')

data.insert(1, 2)
print(f'data sekarang adalah {data}')

data.insert(2, "Han")
print(f'data sekarang adalah {data}')

data.insert(3, False)
print(f'data sekarang adalah {data}')

# menambah di akhir list
data.append("Banget")
print(f'data sekarang adalah {data}')

# menggabungkan list
datanew = [False, 12, "Benar"]
data.extend(datanew)
print(f'data sekarang adalah {data}')

# merubah data 
data[0] = "Hai"
print(f'data sekarang adalah {data}')

# menghapus data
data.remove('Hai')
print(f'data sekarang adalah {data}')