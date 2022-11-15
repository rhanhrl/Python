# operasi list

# memasukan list
listdata = ["Saya", "Adalah", "Seseorang"]
print(f'Terdapat list dengan {listdata}')

listdata.insert(0, "Namaku")
print(f'Data list sekarang adalah {listdata}')

listdata.insert(1, "Raihan")
print(f'Data list sekarang adalah {listdata}')

listdata.insert(2, "Herlambang")
print(f'Data list sekarang adalah {listdata}')

# menggabungkan dua buah list
datalist = [1, 2, 3, True]
datalist.extend(listdata)
print(f'Data list baru dengan {datalist}')

#menghapus anggota list
listdata.remove("Namaku")
print(f'Data list sesudahnya {listdata}')

datalist.remove(True)
print(f'Data list sesudahnya {datalist}')

# indexing
index1 = listdata.index("Raihan")
print(f'Index Raihan = {index1}')

index2 = listdata.index("Herlambang")
print(f'Index ke Herlambang = {index2}')