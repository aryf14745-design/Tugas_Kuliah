print("Selamat datang di program manajemen stok barang")
print("stok barang yang tersedia adalah :")
print("- Buku (10)")
print("- Pensil (20)")
print("- Penghapus (15)")
print("=================================================")
barang = input("Masukkan nama barang : ") .capitalize()
stok = 0

if barang == "Buku":
    stok = 10
elif barang == "Pensil":
    stok = 20
elif barang == "Penghapus":
    stok = 15

while True:
    transaksi = input("Masukkan jenis transaksi (Masuk/Keluar) : ") .capitalize()
    if transaksi == "Masuk":
        jumlah = int(input("Jumlah barang yang ingin masuk : "))
        stok += jumlah
        print(f"Stok {barang} setelah transaksi masuk :{stok}")
    elif transaksi == "Keluar":
        jumlah = int(input("Jumlah barang yang ingin keluar : "))
        if jumlah <= stok:
            stok -= jumlah
            print(f"Stok {barang} setelah transaksi keluar : {stok}")
        else:
            print(f"Maaf, stok {barang} tidak cukup. Stok tersedia: {stok}")
            
    print(f"Stok {barang} sekarang :{stok}")

    lanjut = input("Apakah Anda ingin melakukan transaksi lagi? (Ya/Tidak) : ") .capitalize()
    if lanjut == "Tidak":
        print("Terima kasih telah berkunjung.")
        break

