# membuat program luas dan keliling persegi panjang

import os

os.system('cls') # os adalah salah satu library dari python. cls untuk windows clear untuk mac
def header():
    "header fungsi"

    # header
    print(f"{'PROGRAM LUAS DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

def input_user():
    "input user fungsi"
    LEBAR = int(input("masukan nilai lebar ? "))
    PANJANG = int(input("masukan nilai panjang ? "))

    return LEBAR,PANJANG

def hitung_luas(lebar, panjang):
    "luas fungsi"
    return lebar*panjang

def hitung_keliling(lebar, panjang):
    "keliling fungsi"
    return 2*(lebar + panjang)

def display(message, value):
    "display fungsi"
    print(f"hasil perhitungan {message} = {value}")

# Program utamanya
while True:
    header()
    LEBAR, PANJANG = input_user()
    LUAS = hitung_luas(LEBAR, PANJANG)
    KELILING = hitung_keliling(LEBAR, PANJANG)
    question = input("luas/keliling? ") # opsional

    if question == "luas":
        display("luas = ", LUAS)
    elif question == "keliling":
        display("keliling", KELILING)

    isContinue = input("lanjut (ya/tidak)? ")
    if isContinue == "tidak":
        break
print("program selesai")