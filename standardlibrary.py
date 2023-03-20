import datetime

datawaktu = datetime.datetime.now()
print(datawaktu)
print(f"data waktu = {datawaktu}")
print(f"data tahun = {datawaktu.year}")
print(f"data hari = {datawaktu.strftime('%A')}")

from collections import Counter

data  = ['a', 'b', 'c', 'd', 'a', 'b', 'b']

count = 0

for i in data:
    if i == "a":
        count +=1
print(count)

count2 = 0

for i in data :
    if i == "b":
        count2 += 1
print(count2)

datacount = Counter(data)
print(f"data count = {datacount}")
print(f"data count a = {datacount['a']}")
print(f"data count b = {datacount['b']}")