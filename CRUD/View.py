from . import Operasi

def createConsole():
    print("\n\n"+"="*100)
    print("Silahkan Tambah Data Film")
    pembuat = input("Pembuat\t: ")
    judul = input("Judul\t: ")
    while True:
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun Harus (yyyy), Silahkan Masukan Tahun Lagi")
        except:
            print("Tahun Harus Angaka, Silahkan Masukan Tahun Lagi (yyyy)")

    Operasi.create(tahun,judul,pembuat)
    print("\nBerikut Adalah Data Baru Anda")    
    readConsole()  


def readConsole():
    dataFile = Operasi.read()

    index = "No"
    judul = "Judul"
    pembuat = "Pembuat"
    tahun = "Tahun"

    # header
    print("\n"+"="*100)
    print(f"{index:4} | {judul:40} | {pembuat:40} | {tahun:5}")
    print("-"*100)
    
    # data
    for index,data in enumerate(dataFile):
        dataBreak = data.split(",")
        pk = dataBreak[0]
        dateAdd = dataBreak[1]
        judul = dataBreak[2]
        pembuat = dataBreak[3]
        tahun = dataBreak[4]
        print(f"{index+1:4} | {judul:.40} | {pembuat:.40} | {tahun:4}",end="")


    # footer
    print("="*100+"\n")


def updateConsole():
    readConsole()

    while True:
        print("Silahkan Pilih Nomer Buku Yang Ingin Diupdate")
        noFilm = int(input("Nomor Film: "))

        dataFilm = Operasi.read(index=noFilm)

        if dataFilm:
            break
        else:
            print("Nomot Tidak Valid, Silahkan Masukan Lagi")

    dataBreak = dataFilm.split(",")
    pk = dataBreak[0]
    dateAdd = dataBreak[1]
    judul = dataBreak[2]
    pembuat = dataBreak[3]
    tahun = dataBreak[4][:-1]

    while True:
        # Data yang ingin diupdate
        print("\n"+"="*100)
        print("Silahkan Pilih Data Apa Yang Ingin Diubah")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Pembuat\t: {pembuat:.40}")
        print(f"3. Tahun\t: {tahun:4}")

        # Memilih opsi update
        userOption = input("Pilih Data [1,2,3]: ")
        print("\n"+"="*100)
        match userOption:
            case "1": judul = input("Judul\t: ") 
            case "2": pembuat = input("Pembuat\t: ") 
            case "3": 
                while True:
                    try:
                        tahun = int(input("Tahun\t: "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("Tahun Harus (yyyy), Silahkan Masukan Tahun Lagi")
                    except:
                        print("Tahun Harus Angaka, Silahkan Masukan Tahun Lagi (yyyy)")
            case _: print("Data Index Tidak Cocok")
        
        print("Data Baru Anda")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Pembuat\t: {pembuat:.40}")
        print(f"3. Tahun\t: {tahun:4}")
        isDone = input("Apakah Data Sudah Sesuai (y/n)? ")

        if isDone == "y" or isDone == "Y":
            break
    Operasi.update(noFilm,pk,dateAdd,tahun,judul,pembuat)