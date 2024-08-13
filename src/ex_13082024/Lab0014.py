# list
my_shopping_list = ["milk", "bread", "apple"]
print(my_shopping_list)
positive_num_list = [39, 34, 23, 323]
print(positive_num_list)

name ="ANkita"
print(name.upper())
print(name.lower())
print(len(name))

# if have to add int to strng we have to convert int to string
say = "door"
a = say + str(2)
print(a)

# concating
first_name = "Chandler"
last_name ="Bing"
last_name = first_name + last_name
print(last_name)

# type=none
how_many_planes_i_have = None
print(type(how_many_planes_i_have)) # NoneType
# null is not present in Python

# id
age = 10
age1 = 10
age2 = 11
print(id(age)) # 4336051480
print(id(age1))
print(id(age2)) # 433603232