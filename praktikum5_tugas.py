import os

data_mahasiswa = {}

while True:
    os.system("clear")
    print(f"{'PROGRAM NILAI MAHASISWA':^70}")
    print("="*70)
    print("Silahkan pilih menu :")
    i = input("(T)ambah | (U)bah | (H)apus | (C)ari | (L)ihat | (K)eluar : ")

    #Tambah data
    if i.lower() == 't':
        print("Silahkan isi data di bawah ini,")
        nama = input("Nama           : ")
        nim = int(input("NIM            : "))
        uts = int(input("Nilai UTS      : "))
        uas = int(input("Nilai UAS      : "))
        tugas = int(input("Nilai Tugas    : "))
        nilai_akhir = tugas*0.30 + uts*0.35 + uas*0.35
        data_mahasiswa[nama] = nim, uts, uas, tugas, nilai_akhir

        print("-"*70)
        print(f"|{'Nama':^15}|{'NIM':^10}|{'UTS':^8}|{'UAS':^8}|{'Tugas':^8}|{'Nilai Akhir':^14}|")
        print("="*70)
        print(f"|{nama:^15}|{nim:^10}|{uts:^8}|{uas:^8}|{tugas:^8}|{nilai_akhir:^14.2f}|")
        print("-"*70)

        is_done = input("Data berhasil di tambahkan, lanjutkan (y/n) : ")
        if is_done == 'n':
            break

    #Ubah data
    elif i.lower() == 'u':
        print("Silahkan masukkan nama yang akan di ubah,")
        nama = input("Nama           : ")
        if nama in data_mahasiswa.keys():
            nim = int(input("NIM            : "))
            uts = int(input("Nilai UTS      : "))
            uas = int(input("Nilai UAS      : "))
            tugas = int(input("Nilai Tugas    : "))
            nilai_akhir = tugas*0.30 + uts*0.35 + uas*0.35
            data_mahasiswa[nama] = nim, uts, uas, tugas, nilai_akhir

            print("-"*70)
            print(f"|{'Nama':^15}|{'NIM':^10}|{'UTS':^8}|{'UAS':^8}|{'Tugas':^8}|{'Nilai Akhir':^14}|")
            print("="*70)
            print(f"|{nama:^15}|{nim:^10}|{uts:^8}|{uas:^8}|{tugas:^8}|{nilai_akhir:^14.2f}|")
            print("-"*70)


        else:
            print("Nama {0} tidak ditemukan!!!".format(nama))
        
        is_done = input("Apakah anda ingin melanjutkan (y/n) : ")
        if is_done == 'n':
            break

    #Hapus Data
    elif i.lower() == 'h':
        print("Silahkan masukkan nama yang akan di hapus,")
        nama = input("Nama           : ")
        if nama in data_mahasiswa.keys():
            del data_mahasiswa[nama]
            print("Data {0} berhasil di hapus".format(nama))

        else:
            print("Nama {0} tidak ditemukan!!!".format(nama))

        is_done = input("Apakah anda ingin melanjutkan (y/n) : ")
        if is_done == 'n':
            break

    #Cari Data
    elif i.lower() == 'c':
        print("Silahkan masukkan nama yang akan di cari,")
        nama = input("Nama           : ")
        if nama in data_mahasiswa.keys():
            print("-"*70)
            print(f"|{'DAFTAR MAHASISWA':^68}|")
            print("-"*70)
            print(f"|{'Nama':^15}|{'NIM':^10}|{'UTS':^8}|{'UAS':^8}|{'Tugas':^8}|{'Nilai Akhir':^14}|")
            print("="*70)
            print(f"|{nama:^15}|{nim:^10}|{uts:^8}|{uas:^8}|{tugas:^8}|{nilai_akhir:^14.2f}|")
            print("-"*70)
        else:
            print("Nama {0} tidak ditemukan!!!".format(nama))

        is_done = input("Apakah anda ingin melanjutkan (y/n) : ")
        if is_done == 'n':
            break

    #Lihat Data
    elif i.lower() == 'l':
        if data_mahasiswa.items():
            print("-"*70)
            print(f"|{'DAFTAR MAHASISWA':^68}|")
            print("-"*70)
            print(f"|{'No':^4}|{'Nama':^15}|{'NIM':^10}|{'UTS':^7}|{'UAS':^7}|{'Tugas':^7}|{'Nilai Akhir':^12}|")
            print("="*70)
            j = 0
            for k in data_mahasiswa.items():
                j+=1
                print("|{no:^4}|{0:^15}|{1:^10}|{2:^7}|{3:^7}|{4:^7}|{5:^12.2f}|".format(k[0][:13], k[1][0], k[1][1], k[1][2], k[1][3], k[1][4], no=j))
                print("-"*70)
                # print(f"| {no:2d} | {0:15s} | {1:15d} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |"
                #       .format(y[0][:13], y[1][0], y[1][1], y[1][2], y[1][3], y[1][4], no=i))
                # print("=" * 60)
        else:
            print("-"*70)
            print(f"|{'DAFTAR MAHASISWA':^68}|")
            print("-"*70)
            print(f"|{'Nama':^15}|{'NIM':^10}|{'UTS':^8}|{'UAS':^8}|{'Tugas':^8}|{'Nilai Akhir':^14}|")
            print("="*70)
            print(f"|{'DATA TIDAK DITEMUKAN':^68}|")
            print("-"*70)

        is_done = input("Apakah anda ingin melanjutkan (y/n) : ")
        if is_done == 'n':
            break
    
    #Keluar
    elif i.lower() == 'k':
        break

    else:
        print("Silahkan pilih menu yang tersedia!!!")
        is_done = input("Apakah anda ingin melanjutkan (y/n) : ")
        if is_done == 'n':
            break
