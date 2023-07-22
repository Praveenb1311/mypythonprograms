import os

text = input("Please enter the text to find a file in directory: ")
path = input(("Please provid the file path: "))

# os.chdir is the path:

def getfiles(path):
    x = 0
    os.chdir(path)
    files = os.listdir() # to print the files
    for file_name in files:
        abs_path = os.path.abspath(file_name)
        if os.path.isdir(abs_path):
            getfiles(abs_path)
        if os.path.isfile(abs_path):
            x = open(file_name, "r")
            if text in x.read():
                x = 1
                print(text + "found in")
                final_path = os.path.abspath(file_name)
                print(final_path)
                return True
    if x == 1:
        print(text + "not found! ")
        return False
getfiles(path)