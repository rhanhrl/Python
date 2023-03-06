# membuat fungsi dengan argument

def manusia(nama):
    print(f"selamat datang {nama}")
manusia("Raihan")
print('\n')

def matematika(angka1, angka2):
    hasil = angka1 + angka2
    hasil2 = angka1 - angka2
    hasil3 = angka1 * angka2
    hasil4 = angka1 // angka2
    print(f"angka {angka1} + angka {angka2} = {hasil}")
    print(f"angka {angka1} - angka {angka2} = {hasil2}")
    print(f"angka {angka1} * angka {angka2} = {hasil3}")
    print(f"angka {angka1} : angka {angka2} = {hasil4}")
matematika(12,2)
print('\n')

def data(list_peserta):
    datapeserta = list_peserta.copy()
    for peserta in datapeserta:
        print(f"yang terhormat {peserta}")
psrt = ["raihan", "herlambang"]
data(psrt)