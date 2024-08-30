my_list=[0, 1, 3, 2, 4, 5, 7, 8, 9, 10, 'Pramod']

my_copy_list = my_list.copy()
print(my_copy_list)
print(my_list)

my_list.clear()
print(my_list)
print(my_copy_list)

my_copy_list.remove("Pramod")
print(my_copy_list)

my_copy_list.sort()
print(my_copy_list)

my_copy_list.sort(reverse=False)
print(my_copy_list)

my_copy_list.reverse()
print(my_copy_list)

name = "dipika"
name = name.upper()
print(name)