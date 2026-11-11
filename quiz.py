#input
print ("Nama Nama Mahasiswa")
print ("Andi")
print ("Budi")
print ("Citra")
nama = input("Masukkan Nama Mahasiswa :")

#proses
if nama == "Andi":
    target = 70
elif nama == "Budi":
    target = 75
elif nama == "Citra":
    target = 80
else:
    target = 0

if target == 0 :
    print("Nama Mahasiswa Tidak Ada")
else :
    print("Target Nilai : ", target)
    percobaan = 0 
    lulus = False

    while percobaan <3 and not lulus:
        nilai = int(input("Masukkan Nilai Ujian :"))
        percobaan += 1 
        if nilai >= target : 
            lulus = True
            print(nama,"Lulus")
            if percobaan == 3 :
                print("Lulus setelah 3 kali percobaan")
        else :
            print(nama, "Tidak Lulus")
    if not lulus :
        print(nama, "Tidak lulus setelah 3 kali percobaan")
