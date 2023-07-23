# looping dictionary

friends = {
    "key1" : "value1",
    "key2" : "value2",
    "key3" : "value3"
}

#menggunakan for pada dictionary
for teman in friends:
    print(teman)
print("\n")

# iterable pada dictionary
keys = friends.keys()
print(keys)

for key in friends.keys():
    print(friends.get(key))
print("\n")

values = friends.values()
print(values)

for value in friends.values():
    print(value)
print("\n")

items = friends.items()
print(items)

for item in friends.items():
    print(item)
print("\n")

for key,value in friends.items():
    print(f"key = {key} value = {value}")
