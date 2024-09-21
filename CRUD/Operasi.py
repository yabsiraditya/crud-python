from time import time
from . import Database
from.Util import randomString
import time

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

def read():
    try:
        with open(Database.DB_NAME,'r') as file:
            content = file.readlines()
            return content
    except:
        print("Data Base Error")
        return False