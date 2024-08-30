my_list = [1, 2, 3]

# append()
my_list.append(4)  # Append object to the end of the list.
my_list.append(5)
my_list.append(6)
my_list.append("ankita")
print(my_list)

# extend()
my_list.extend([7, 8, 9])
my_list.extend([10])
my_list.extend(["Pramod"])
my_list.extend(["ankita"])
print(my_list)
print(len(my_list))

# insert()
my_list.insert(1, "Dutta")
print(my_list)
print(len(my_list))

my_list[1] = "Amit"
print(my_list)

my_list[1] = 24
print(my_list)

my_list.insert(0, 0)
print(my_list)
my_list.insert(-1,"Lucky")
print(my_list)

# remove()
my_list.remove(24)
print(my_list)  # This will not  work