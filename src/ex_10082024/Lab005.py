# 📕 Keywords &  Identifiers
# import keyword
# print(keyword.kwlist)
# cannot use as variable name
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
# 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
# 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
# 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# Variable
# It is used to store the value  - containers

age=3
print(age)
age="Ankita"
print(age)

# age - variable - identifer
# 123 = 34 -> Not possible - A-Z, a-z

# They start with a letter (A-Z or a-z)
# an underscore (_) followed by zero or more letters,
# underscores, and digits (0-9).
# Python is case-sensitive,
# so myVariable and myvariable are two different identifiers.

a = 10
_ = 45
_ = _+1
print(_)

abc123 = 78
#123abc = 90
_pramod = "amit"
_abc = 23
#$123 = 67
#&123 = 23


pi = 3.14
name = "Ankita"
isGood = True
print(type(name))
print(type(isGood))
print(type(pi))

complex_number = 2 + 3j
print(complex_number.real)
print(complex_number.imag)
# Dynamically typed
# At the run time, data of the variable can be changed. and you don't need to
# mention the data type - Python - Int is very smart
age = 45
print(age)
print(type(age))
age = "Ankita"
print(age)
print(type(age))