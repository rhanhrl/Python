def fungsi(nama,tinggi, berat):
    print(f"nama = {nama} tinggi = {tinggi} berat = {berat}")
fungsi("raihan", 170, 55)
print('\n')


def fungsi(data_list):
    data = data_list.copy()
    nama = [0]
    tinggi = [1]
    berat = [2]
    print(f"nama = {nama} tinggi = {tinggi} berat = {berat}")
fungsi(["raihan", 170, 58])
print('\n')

# introduction with args
def data(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"nama = {nama} tinggi = {tinggi} berat = {berat}")
data("raihan", 175, 60)
print('\n')


# studi kasus
def tambah(*data):
    #data tipenya tuple, bisa diiterasikan
    output = 0
    for angka in data:
        output += angka
    return output
hasil = tambah(1,2,3,4,5)
print(hasil)
