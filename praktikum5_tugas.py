import os

mahasiswa_template = {
    'nama':'nama',
    'nim':'000000000',
    'uts':0,
    'uas':0,
    'tugas':0,
    'nilai_akhir':0
}

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
        mahasiswa = dict.fromkeys(mahasiswa_template.keys())

        mahasiswa['nama'] = input("Nama           : ")
        mahasiswa['nim'] = int(input("NIM            : "))
        mahasiswa['uts'] = int(input("Nilai UTS      : "))
        mahasiswa['uas'] = int(input("Nilai UAS      : "))
        mahasiswa['tugas'] = int(input("Nilai Tugas    : "))
        NAMA = mahasiswa['nama']
        NIM = mahasiswa['nim']
        UTS = mahasiswa['uts']
        UAS = mahasiswa['uas']
        TUGAS = mahasiswa['tugas']
        mahasiswa['nilai_akhir'] = TUGAS*0.30 + UTS*0.35 + UAS*0.35
        NILAI_AKHIR = mahasiswa['nilai_akhir']

        KEY = mahasiswa['nim']
        data_mahasiswa.update({KEY:mahasiswa})
        print(data_mahasiswa)

        print("-"*70)
        print(f"|{'Nama':^15}|{'NIM':^10}|{'UTS':^8}|{'UAS':^8}|{'Tugas':^8}|{'Nilai Akhir':^14}|")
        print("="*70)
        print(f"|{NAMA:^15}|{NIM:^10}|{UTS:^8}|{UAS:^8}|{TUGAS:^8}|{NILAI_AKHIR:^14.2f}|")
        print("-"*70)
 
        is_done = input("Data berhasil di tambahkan, lanjutkan (y/n) : ")
        if is_done == 'n':
            break

    #Lihat Data
    elif i.lower() == 'l':
        print("-"*70)
        print(f"|{'DAFTAR MAHASISWA':^68}|")
        print("-"*70)
        print(f"|{'No':^4}|{'Nama':^15}|{'NIM':^10}|{'UTS':^7}|{'UAS':^7}|{'Tugas':^7}|{'Nilai Akhir':^12}|")
        print("="*70)
        no = 1
        for mahasiswa in data_mahasiswa.items():
            print(f"|{no:^4}|{NAMA:^15}|{KEY:^10}|{UTS:^7}|{UAS:^7}|{TUGAS:^7}|{NILAI_AKHIR:^12.2f}|")            
            no += 1

        is_done = input("Apakah anda ingin melanjutkan (y/n) : ")
        if is_done == 'n':
            break

    #Ubah data
    elif i.lower() == 'u':
        print("Silahkan masukkan NIM yang akan di ubah datanya,")
        nim = int(input("NIM           : "))
        if nim in data_mahasiswa.keys():
            mahasiswa['uts'] = int(input("Nilai UTS      : "))
            mahasiswa['uas'] = int(input("Nilai UAS      : "))
            mahasiswa['tugas'] = int(input("Nilai Tugas    : "))
            NAMA = mahasiswa['nama']
            NIM = mahasiswa['nim']
            UTS = mahasiswa['uts']
            UAS = mahasiswa['uas']
            TUGAS = mahasiswa['tugas']
            mahasiswa['nilai_akhir'] = TUGAS*0.30 + UTS*0.35 + UAS*0.35
            NILAI_AKHIR = mahasiswa['nilai_akhir']

            KEY = mahasiswa['nim']
            data_mahasiswa.update({KEY:mahasiswa})
            
            print("-"*70)
            print(f"|{'Nama':^15}|{'NIM':^10}|{'UTS':^8}|{'UAS':^8}|{'Tugas':^8}|{'Nilai Akhir':^14}|")
            print("="*70)
            print(f"|{NAMA:^15}|{NIM:^10}|{UTS:^8}|{UAS:^8}|{TUGAS:^8}|{NILAI_AKHIR:^14.2f}|")
            print("-"*70)


        else:
            print(f"NIM {nim} tidak ditemukan!!!")
        
        is_done = input("Apakah anda ingin melanjutkan (y/n) : ")
        if is_done == 'n':
            break

    #Hapus Data
    elif i.lower() == 'h':
        print("Silahkan masukkan nama yang akan di hapus,")
        nim = int(input("Nama           : "))
        if nim in data_mahasiswa.keys():
            del data_mahasiswa[nim]
            print(f"Data NIM {nim} berhasil di hapus")

        else:
            print(f"NIM {nim} tidak ditemukan!!!")

        is_done = input("Apakah anda ingin melanjutkan (y/n) : ")
        if is_done == 'n':
            break

    #Cari Data
    elif i.lower() == 'c':
        print("Silahkan masukkan NIM yang akan di cari,")
        nim = int(input("NIM           : "))
        # print(data_mahasiswa.get(j))
        if nim in data_mahasiswa.keys():
            print("-"*70)
            print(f"|{'DAFTAR MAHASISWA':^68}|")
            print("-"*70)
            print(f"|{'Nama':^15}|{'NIM':^10}|{'UTS':^8}|{'UAS':^8}|{'Tugas':^8}|{'Nilai Akhir':^14}|")
            print("="*70)
            print(f"|{NAMA:^15}|{NIM:^10}|{UTS:^8}|{UAS:^8}|{TUGAS:^8}|{NILAI_AKHIR:^14.2f}|")
            print("-"*70)
        else:
            print(f"NIM {nim} tidak ditemukan!!!")

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
