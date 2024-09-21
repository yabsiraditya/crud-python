from . import Operasi

DB_NAME = "data.txt"
TEMPLATE = {
    "pk":"xxxxxx",
    "dateAdd":"yyyy-mm-dd",
    "judul":255*" ",
    "pembuat":255*" ",
    "tahun":"yyyy"
}

def init_console():
    try:
        with open("DB_NAME","r") as file:
            print("Data tersedia, init done!")
    except:
        print("Data base tidak ditemukan, silahkan buat database baru")
        Operasi.createFirstData()