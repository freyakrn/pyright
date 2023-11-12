print("Hello World")

#data dengan perulangan

data = []
while True :
  print("=== Sistem Menu ===")
  print("1. Input nama")
  print("2. Tampilkan nama")
  print("3. Hapus nama")
  print("4. Keluar")

menu = input("Masukkan menu yang diinginkan [1-4] : ")
if menu == "1" :
  inputNama = input("Masukkan nama : ")
  data.append(inputNama)
elif menu == "2" :
  cariNama = input("Masukkan nama : ")
  for i in data :
    if i == cariNama :
      print("Nama ", i, "ada")
    else :
      print("Nama ", cariNama, "tidak ada")
elif menu == "3" :
  cekNama = input("Masukkan nama : ")
  if cekNama in data :
    data.remove(cekNama)
    print(cekNama, "telah dihapus dari data")
  else :
    print(cekNama, "tidak ada dalam data yang akan dihapus")
elif menu == "3" :
  print("Program Selesai")
  break
  
