from pathlib import Path

filename = input("Enter file name: ")
pathname = Path(filename)
if pathname.exists(): 
    file = open(filename)
    content = file.read()
    print(content)
    file.close()
else:
    print("Error: File doesn't exist")
