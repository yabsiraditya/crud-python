import os
import CRUD as CRUD

if __name__ == "__main__":
    sistemOperasi = os.name

    match sistemOperasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    print("Selamat Datang Di Program")
    print("Database Film")
    print("=========================")

    # cek database ada atau tidak
    CRUD.init_console

    while True:
        match sistemOperasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")

        print("Selamat Datang Di Program")
        print("Database Film")
        print("=========================")

        print(f"1. Read Data")
        print(f"2. Create Data")
        print(f"3. Update Data")
        print(f"4. Delete Data")
        print("=========================")

        userOption = input("Masukan Opsi : ")

        match userOption:
            case "1": CRUD.readConsole()
            case "2": CRUD.createConsole()
            case "3": CRUD.updateConsole()
            case "4": CRUD.deleteConsole()
            
        isDone = input("Apakah Selesai (y/n)? ")

        if isDone == "y" or isDone == "Y":
            break

    print("Program Selesai, Terima Kasih")