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