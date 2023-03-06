import datetime

mahasiswa1 = {
    'nama':'Raihan',
    'jurusan':'Teknik Informatika',
    'nim':2130511005
}
mahasiswa2 = {
    'nama':'Herlambang',
    'jurusan':'Teknik Informatika',
    'nim':2130511006
}
data_mahasiswa = {
    'M001':mahasiswa1,
    'M002':mahasiswa2
}
print(f"{data_mahasiswa}\n")

print(f"{'KEY':<10} {'NAMA':^15} {'JURUSAN':^15} {'NIM':^30}")

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa

    NAMA = data_mahasiswa[KEY]['nama']
    JURUSAN = data_mahasiswa[KEY]['jurusan']
    NIM = data_mahasiswa[KEY]['nim']
    print(f"{KEY:<10} {NAMA:^15} {JURUSAN:^15} {NIM:^30}")
quit()