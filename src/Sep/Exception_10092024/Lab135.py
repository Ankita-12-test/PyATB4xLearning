import os

full_path_file = os.path.join("\Users\Ankita dhamane\PycharmProjects\PyATB4xLearning\src\Sep\Exception_10092024\Anks", "Ankita.txt")
file = open(full_path_file, 'r')
content = file.read()
print(content)