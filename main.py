import os
import CRUD as CRUD

if __name__ == "__main__":
    sistemOperasi = os.name

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

        print("\n=========================\n")

        match userOption:
            case "1": print("Read Data")
            case "2": print("Create Data")
            case "3": print("Update Data")
            case "4": print("Delete Data")
            
        print("\n=========================\n")
        isDone = input("Apakah Selesai (y/n)? ")

        if isDone == "y" or isDone == "Y":
            break

    print("Program Selesai, Terima Kasih")