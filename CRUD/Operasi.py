from time import time
from . import Database
from.Util import randomString
import time
import os

def create(tahun,judul,pembuat):
    data = Database.TEMPLATE.copy()

    data["pk"] = randomString(6)
    data["dateAdd"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["pembuat"] = pembuat + Database.TEMPLATE["pembuat"][len(pembuat):]
    data["tahun"] = str(tahun)

    dataStr = f'{data["pk"]},{data["dateAdd"]},{data["judul"]},{data["pembuat"]},{data["tahun"]}\n'

    try:
        with open(Database.DB_NAME,'a',encoding='utf-8') as file:
            file.write(dataStr)
    except:
        print("Data gagal ditambahkan")


def createFirstData():
    judul = input("Judul Film : ")
    pembuat = input("Pembuat Film : ")
    while True:
            try:
                tahun = int(input("Tahun\t: "))
                if len(str(tahun)) == 4:
                    break
                else:
                    print("Tahun Harus (yyyy), Silahkan Masukan Tahun Lagi")
            except:
                print("Tahun Harus Angaka, Silahkan Masukan Tahun Lagi (yyyy)")

    data = Database.TEMPLATE.copy()

    data["pk"] = randomString(6)
    data["dateAdd"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["pembuat"] = pembuat + Database.TEMPLATE["pembuat"][len(pembuat):]
    data["tahun"] = str(tahun)

    dataStr = f'{data["pk"]},{data["dateAdd"]},{data["judul"]},{data["pembuat"]},{data["tahun"]}\n'

    try:
        with open(Database.DB_NAME,'w',encoding='utf-8') as file:
            file.write(dataStr)
    except:
        print("Data gagal ditambahkan")

def read(**kwargs):
    try:
        with open(Database.DB_NAME,'r') as file:
            content = file.readlines()
            jumlahFilm = len(content)
            if "index" in kwargs:
                indexFilm = kwargs["index"]-1
                if indexFilm < 0 or indexFilm > jumlahFilm:
                    return False
                else:
                    return content[indexFilm]
            else:
                return content
    except:
        print("Data Base Error")
        return False
    

def update(noFilm,pk,dateAdd,tahun,judul,pembuat):
    data = Database.TEMPLATE.copy()

    data["pk"] = pk
    data["dateAdd"] = dateAdd
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["pembuat"] = pembuat + Database.TEMPLATE["pembuat"][len(pembuat):]
    data["tahun"] = str(tahun)

    dataStr = f'{data["pk"]},{data["dateAdd"]},{data["judul"]},{data["pembuat"]},{data["tahun"]}\n'

    dataLen = len(dataStr)

    try:
        with(open(Database.DB_NAME,'r+',encoding="utf-8")) as file:
            file.seek(dataLen*(noFilm-1))
            file.write(dataStr)
    except:
        print("Error Saat Mengupdate Data")

def delete(noFilm):
    try:
        with open(Database.DB_NAME,'r') as file:
            counter = 0

            while True:
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == noFilm - 1:
                    pass
                else:
                    with(open("dataTemp.txt",'a',encoding="utf-8")) as tempFile:
                        tempFile.write(content)
                counter += 1
    except:
        print("Database Error Gagal Menghapus")

    os.rename("dataTemp.txt",Database.DB_NAME)