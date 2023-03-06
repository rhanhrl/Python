# return digunakan untuk mengembalikan nilai

def bilangan(angka):
    hasil = angka**2
    print(f"kuadrat dari 5 adalah {hasil}")
    return hasil
y = bilangan(5)
print(f"sehingga {y} adalah kuadrat dari 5\n")

def bilangan2(angka2):
    hasil2 = angka2**2
    print(f"kuadrat dari 6 adalah {hasil2}")
    return hasil2
x = bilangan2(6)
print(f"sehingga {x} adalah kuadrat dari 6\n")


def bilangan3(angka3, angka4):
# return dengan multi input
    return angka3 + angka4;
a = bilangan3(4,2)
print(f"{a}\n")

def bilangan4(angka4, angka5):
    hasil3 = angka4 + angka5
    hasil4 = angka4 - angka5
    hasil5 = angka4 * angka5
    hasil6 = angka4 / angka5
    return hasil3, hasil4, hasil5, hasil6
c,e,f,g = bilangan4(16,6)
print(f"16 ditambah 6 = {c}")
print(f"16 dikurang 6 = {e}")
print(f"16 dikali 6 = {f}")
print(f"16 dibagi 6 = {g}")