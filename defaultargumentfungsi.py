# menggunakan nilai default
#def hai(pesan="hola"):
    #print(f"{pesan}")
#hai()

#contoh 1
def manusia(nama, pesan="selamat datang "):
    print(f"hai {nama}, {pesan}\n")
manusia("Raihan")

#contoh 2
def angka(bilangan, pangkat=2):
    hasil = bilangan**pangkat
    return hasil
print(f"5 pangkat 3 adalah {angka(5)}")
print(f"6 pangkat 3 adalah {angka(6,3)}")

#contoh 3
hasil = angka(bilangan=7, pangkat=3)
print(hasil)

# contoh 4
def integer(input1=1, input2=2, input3=3):
    hasil = input1+input2+input3
    return hasil
print(integer())
print(integer(input2=10))
