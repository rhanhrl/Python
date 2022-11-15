list_a = ["Herlambang", "Roy", "Yes"]
print(list_a)

list_b = list_a

print(list_b)

list_a[1] = "Raihan"

list_b.sort()
print(f'A = {list_a}')
print(f'B = {list_b}')

print(f'Address a{list_a}')
print(f'Addreess b{list_b}')

print(f'Address a = {hex(id(list_a))}')
print(f'Address b = {hex(id(list_b))}')

list_c = list_a.copy()
print(f'Address a = {hex(id(list_a))}')
print(f'Address b = {hex(id(list_b))}')
print(f'Address c = {hex(id(list_c))}')

print(f'Address a = {list_a}')
print(f'Address b = {list_b}')
print(f'Address c = {list_c}')