import os
#fungsi ascending
def urutasc(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j]>a[j+1]:
                simpan=a[j]
                a[j]=a[j+1]
                a[j+1]=simpan
    print(a)
#fungsi Descending
def urutdesc(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j]<a[j+1]:
                simpan=a[j]
                a[j]=a[j+1]
                a[j+1]=simpan
    print(a)
#pengulangan
while(True):
 
 print("===========================")
 print("program mengurutkan data")
 print("methode Buble sort")

 angka1 = int(input("masukkan angka 1 : "))
 angka2 = int(input("masukkan angka 2 : "))
 angka3 = int(input("masukkan angka 3 : "))
 angka4 = int(input("masukkan angka 4 : "))
 angka5 = int(input("masukkan angka 5 : "))

 print("=====================")
 print("pilihan metode pengurutan")
 print("1.Ascending")
 print("2.Descending")
 pilih = input("masukkan pilihan :")
 bil=[angka1,angka2,angka3,angka4,angka5]
 print("Data sebelum diurutkan")
 print(bil)
 print("nilai maksimal : ",max(bil))
 print("niali minimal : ",min(bil))
 print("rata : rata",sum(bil)/len(bil))
 print("Data setelah di urutkan")
 if pilih =="1":
     urutasc(bil)
 elif pilih =="2":
     urutdesc(bil)
 else:
     print("pilihan tidak ada")
     print("===============")
 menu = input("Kembali ke menu utama(Y/N)?")
 if menu == "N" or menu=="n":
        print("selesai terimakasih")
        break
 elif menu == "Y" and menu=="y":
        print("selesai terimakasih")
        break



