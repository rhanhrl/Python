# Komparasi dan logika
# Membuktikan nilai / angka yang kurang dari dan lebih besar dari ataupun sebaliknya

# ++++3------10++++ (Kurang dari 3 atau lebih dari 10)
print(">>>>>>> Komparasi dan Logika <<<<<<<")
Inputan = float(input("1. masukan angka yang kurang dari 3 atau lebih dari 10 ="))
InputUser = (Inputan < 3), (Inputan > 10)
print("angka yang kurang dari 3 atau lebih dari 10 =", InputUser)

# ----3++++++10---- (Lebih dari 3 dan Kurang dari 10)
print("--------------------------------------------")
Inputan2 = float(input("2. masukan angka yang lebih dari 3 dan kurang dari 10 ="))
InputUser2 = (Inputan2 > 3), (Inputan2 < 10)
print("angka yang lebih dari 3 dan kurang dari 10 =", InputUser2)

#----3++++++10++++ (Lebih dari 3 dan Lebih dari 10)
print("------------------------------------------")
Inputan3 = float(input("3. masukan angka yang lebih dari 3 dan lebih dari 10 ="))
InputUser3 = (Inputan3 > 3), (Inputan > 10)
print("angka yang lebih dari 3 dan lebih dari 10 =", InputUser3)

#++++3------10---- (Kurang dari 3 atau Kurang dari 10)
print("--------------------------------------------")
Inputan4 = float(input("4. masukan angka yang kurang dari 3 atau kurang dari 10 ="))
InputUser4 = (Inputan4 < 3), (Inputan4 < 10)
print("angka yang kurang dari 3 atau kurang 10 =", InputUser4)
