# try, except and finally
# file

import os
# full_path = os.getcwd()
# print((full_path))

try:
    full_path = os.getcwd()
    full_path_file = full_path+"\example.txt"
    print(full_path_file)
    file = open(full_path_file, 'r')
    print(file.read())
except Exception as e:
    print(e)
    print("File Not found, fix the path or create a file")
finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)
