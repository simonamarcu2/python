# print("Hello world")
# #prints sends to the terminal

# #string
# x = "this is string"
# #integer
# x = 3
# #floating point
# x = 3.3
# #none
# x = None
# #boolean
# x = True
# y = False

# #how to check a data type
# print(type(x))

# a ="3"
# b = 3
# c = 3.0

# print(len("supercalifragilisticexpialidocious"))

# print("supercalifragilisticexpialidocious" [16])

# print("hello" .upper())
# print("WORLD" .lower())
# print("data" .capitalize())
# print("hello everyone.".count("e"))
# print("hello everyone.".find("v"))
# print("random" .replace("random", "lock"))
# print("team all" .strip("all"))
# #.upper() --- converts string to uppercase
# print("hello".upper())
# #.lower() --- converts string to lowercase
# print("HELLO".lower())
# #.capitalize() --- capitalises a string
# print("hello everyone.".capitalize())
# #.count() --- counts the amount of times a character appears in a string
# print("hello everyone".count("e"))
# #.find() --- locates the index position of parameter.
# print("hello everyone".find("v"))
# #.replace() --- one string with another
# print("hello everyone".replace("everyone", "all"))
# #.strip() --- remove the parameter from the string.
# print("hello everyone".strip("everyone"))



#################################################
# import random

# print(random.random())
# print(random.randint(1, 15))

import time
import random

print(random.randint(1, 10))

timestamp = time.time()
current_time = time.ctime(timestamp)
print(current_time)

from math import ceil, floor
print(ceil(3.4)) # 4
print(floor(3.4)) # 3
