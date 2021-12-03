# print("All Around the World".upper()[7])

# my_name = "Simona"
# my_age = 36
# student = True
# print (my_name, my_age)

# fave_drink = "coffee"
# print("My favourite drink is", fave_drink)
# #format strings
# print("My favourite drink is {}".format(fave_drink))

# print("My name is {} and I love {}".format(my_name, fave_drink))
# print("My name is {} and I am {} years old".format(my_name, my_age))
# #---------------------------------------------------------------------
# #f - strings
# print(f"{my_name}'s fave drink is {fave_drink}.")

#operators
# i = 10
# i = i + 2
# i = i + 5
# i = i + 3
# i += 27
# i +=  4
# print(i)

#activity 1

# name = "Freya"
# age = 26
# color = "turquoise"

# print(f"She is {name} and her age is {age},she likes {color}!")

# breakfast = "cereal"
# lunch = "soup"
# dinner = "chips"

# print(f"Breakfast = {breakfast},Lunch = {lunch},Dinner = {dinner}")

# v1 = "x"
# v2 = "o"
# v3 = " "
# v4 = "x"
# v5 = "x"
# v6 = " "
# v7 = "o"
# v8 = " "
# v9 = " "

# print(f"     |     |     ")
# print(f"  {v1}  |  {v2}  |  {v3}  ")
# print(f"     |     |     ")
# print(f"-----------------")
# print(f"     |     |     ")
# print(f"  {v4}  |  {v5}  |  {v6}  ")
# print(f"     |     |     ")
# print(f"-----------------")
# print(f"     |     |     ")
# print(f"  {v7}  |  {v8}  |  {v9}  ")
# print(f"     |     |     ")

# x = ("|")
# y = ("--------------------")
# space1 = "x"
# space2 = "o"
# space3 = ""
# space4 = "x"
# space5 = "x"
# space6 = ""
# space7 = "o"
# space8 = ""
# space9 = ""
# print(f"     {x}    {x}    {x}")
# print(f"  {space1}  {x}  {space2} {x}  {space3}  {x}")
# print(f"     {x}    {x}    {x}")
# print(f"{y}")
# print(f"     {x}    {x}    {x}")
# print(f"  {space4}  {x}  {space5} {x}  {space6}  {x}")
# print(f"     {x}    {x}    {x}")
# print(f"{y}")
# print(f"     {x}    {x}    {x}")
# print(f"  {space7}  {x}   {space8} {x}  {space9}  {x}")
# print(f"     {x}    {x}    {x}")

#equal
x = 2
#multiplication
x *= 2
# += add
# *= multiplication
# /= divide
# -= minus
# % modulus
# y = 15

# y = 10 % 3
# print(y)

# timestamp = time.time()
# current_time = time.ctime(timestamp)
# print(current_time)


# import time
# import datetime
# name = "Alan"

# bday = datetime.datetime(1985, 7, 16)
# today =datetime.datetime(2021, 9, 21)
# next_bday = datetime.datetime(2022, 7, 16)

# print(today)
# distance = next_bday - today
# print(next_bday)
# print(today - bday)

import datetime

name = "Simona"

my_bday = datetime.date(1985, 7, 16)
today = datetime.date.today()
future = datetime.date(2022, 7, 16)

age_days = future - today
bday_in = future - today

print(f"My name is {name}, I am {age_days} old and it is {bday_in} days until my next birthday.")
