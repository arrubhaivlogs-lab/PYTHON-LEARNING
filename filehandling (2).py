from pathlib import Path
def readfileandfolder():
    path=Path('')
    item=list(path.rglob("*"))
    for i , item in enumerate(item):
        print(f"{i+1} : {item}")
def createfile():
    try:
        readfileandfolder()
        name=input("Enter the name of the file to be created: ")
        p=Path(name)
        if not p.exists():
            with open(p,'w') as fs:
                data=input("do you want to add data to the file? (y/n): ")
                if data.lower() == 'y':
                    file_data=input("Enter the data to be added to the file: ")
                    fs.write(file_data);print("File created with data.")
                else:
                    print("File created without data.")
        else:
            print("File already exists.")            
    except Exception as e:
        print(f"An error occurred: {e}")
def readfile():
    try:
        readfileandfolder()
        name=input("Enter the name of the file to be read: ")
        p=Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                print(fs.read())
                print("File read successfully.")
        else:
            print("File does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
def updatefile():
    try:
        readfileandfolder()
        name=input("Enter the name of the file to be updated: ")
        p=Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing the name of file")
            print("press 2 for overwriting data in the file")  
            print("press 3 for appending data to the file")
            choice = int(input("Enter your choice: "))
            if choice == 1:  
                name2=input("Enter the new name of the file: ")
                p2=Path(name2)
                p.rename(p2)
            elif choice == 2:
                with open(p,'w') as fs:
                    file_data=input("Enter the data to be written to the file: ")
                    fs.write(file_data)
                    print("File overwritten successfully.")
            elif choice == 3:
                with open(p,'a') as fs:
                    file_data=input("Enter the data to be appended to the file: ")
                    fs.write(file_data)
                    print("Data appended successfully.")            
    except Exception as e:
        print(f"An error occurred: {e}")

print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")
choice = int(input("Enter your choice: "))
if choice == 1:
    createfile()
elif choice == 2:
    readfile()
elif choice == 3:
    updatefile()    
elif choice == 4:
    try:
        readfileandfolder()
        name=input("Enter the name of the file to be deleted: ")
        p=Path(name)
        if p.exists() and p.is_file():
            p.unlink()
            print("File deleted successfully.")
        else:
            print("File does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")    