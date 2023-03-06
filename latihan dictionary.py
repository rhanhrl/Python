import datetime
import os
import string
import random

templateMhs = {
    'nama':'raihan',
    'umur':'20 thn',
    'alamat':'sukabumi',
    'ipk':3.40,
    'lahir':datetime.datetime(111, 11, 1)
}

dataMhs = {}

while True:
    os.system('cls')
    #os.system('clear')untuk mac,linux dll
    print(f"{'Selamat datang':^20}")
    print("-"*20)
    mahasiswa = dict.fromkeys(templateMhs.keys())
    mahasiswa['nama'] = input('Masukan nama : ')
    mahasiswa['umur'] = input('Masukan umur : ')
    mahasiswa['alamat'] = input('Masukan alamat : ')
    mahasiswa['ipk'] = float(input('Masukan ipk : '))

    THN_LAHIR = int(input('Masukan tahun lahir (YYY) : '))
    BLN_LAHIR = int(input('Masukan bulan lahir (1-12) : '))
    TGL_LAHIR = int(input('Masukan tanggal lahir (1-31) : '))
    mahasiswa['lahir'] = datetime.datetime(THN_LAHIR, BLN_LAHIR, TGL_LAHIR)

    KEY = ''.join((random.choice(string.ascii_uppercase)for i in range(6)))
    dataMhs.update({KEY:mahasiswa})

    print('\n')
    print(f"{'KEY':<6} {'NAMA':^20} {'UMUR':^10} {'ALAMAT':^15} {'IPK':^10} {'LAHIR':^10}")
    print('-'*80)
    
    for mahasiswa in dataMhs:
        KEY = mahasiswa

        NAMA = dataMhs[KEY]['nama']
        UMUR = dataMhs[KEY]['umur']
        ALAMAT = dataMhs[KEY]['alamat']
        IPK = dataMhs[KEY]['ipk']
        LAHIR = dataMhs[KEY]['lahir'].strftime("%x")

        print(f"{KEY:<6} {NAMA:^20} {UMUR:^10} {ALAMAT:^15} {IPK:^10} {LAHIR:<10}")
    print('\n')

    is_done = input("Lagi? (ya/tidak) : ")

    if is_done == "tidak":
        break
print('Akhir program')