# operator dictionary

dataDict = {
    "key1" : "value1",
    "key2" : "value2"
}
dataPj = len(dataDict)
print(F"panjang data dictionary : {dataPj}")

# mengecek key dictionary
KEY = "key1"
CHECKKEY = KEY in dataDict
print(f"Apakah key1 ada : {CHECKKEY}")

# mengakses value
print(dataDict.get("key2"))
print(dataDict.get("key3"))
print(dataDict.get("key3", "tidak ada"))

# mengupdate data
dataDict.update({"key2":"value"})
print(dataDict)
dataDict.update({"key3":"value3"})
print(dataDict)

# menghapus data 
del dataDict["key1"]
print(dataDict)

#latihan

dataDict2 = {
    "key1" : "value1",
    "key2" : "value2",
    "key3" : "value3"
}

KEY1 = "key1"
CHECKKEY1 = KEY1 in dataDict2
print(CHECKKEY1)

print(dataDict2)

print(dataDict2["key3"]) # mengakses melalui key

print(dataDict2.get(
    "key3"
)) # menggunakan get
dataDict2.update({
    "key 4" : "value4"
}) # mengupdate
print(dataDict2)
