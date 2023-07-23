
dataDict = {
    "key1" : "value1",
    "key2" : "value2",
    "key3" : "value3"
}

#copy dictionary
dataDict2 = dataDict.copy()
print(f"{dataDict2}")
print(f"{dataDict}")

dataDict2.update({"key1":"value"})
print(dataDict2)
print(f"{dataDict2}")

#pop dictionary (berdasarkan key)
dataDict3 = dataDict2.pop("key3")
print(f"key 3 : ", dataDict3)
print(dataDict2)

#pop item dictionary (yang terakhir)
dataDict4 = dataDict2.popitem()
print(f"{dataDict4}")
