n = int(input())
stok = {}
list_bunga = []

for i in range(n):
  nama_bunga = input()
  jumlah = int(input())
  stok[nama_bunga.lower()] = jumlah
  list_bunga.append(nama_bunga)

m = int(input())

for i in range(m):
  nama_bunga = input().lower()
  jumlah = int(input())
  if(nama_bunga not in stok.keys()):
      print("Pesanan tidak bisa diproses")
  elif(stok[nama_bunga] < jumlah):
      print("Pesanan tidak bisa diproses")
  else:
      print("Pesanan bisa diproses")
      stok[nama_bunga] -= jumlah

for i in range(n):
  nama_bunga = list_bunga[i]
  print(nama_bunga, stok[nama_bunga.lower()])