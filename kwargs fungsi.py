# keyword args dalam fungsi

def data(**kwargs):
    "kwargs fungsi"
    nama = kwargs["nama"]
    umur = kwargs["umur"]
    alamat = kwargs["alamat"]
    print(f"nama {nama} dengan umur {umur} dan alamat {alamat}")
data(nama="raihan", umur=20, alamat="sukabumi")

# studi kasus
def math(*args, **kwargs):
    "studi kasus"
    output = 0
    if kwargs["option"]=="tambah":
        for angka in args:
            output += angka
    elif kwargs["option"]=="kali":
        output = 1
        for angka in args:
            output *= angka
    else:
        print("operasi gagal")
    return output
hasil = math(1,2,3,4,5, option = "tambah")
print(f"hasil penambahan {hasil}")
hasil = math(1,2,3,4,5, option = "kali")
print(f"hasil perkalian {hasil}")