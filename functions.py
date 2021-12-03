

# def say_hello():
#   print("Hello")

# say_hello()


# def cash_withdrawal(amount, account):
#     print(f"Withdrawing £{amount} from account number {account}...")

# cash_withdrawal(300, 50449921)
# cash_withdrawal(5000, 50449921)

# def shout(parameter):
#     print(f"{parameter}!".upper())

# shout("sorry, I can't quite hear you?")

# def coffee_order(size, type):
#   print(f"You have a {size} coffee {type}. It's that all?")

# coffee_order("medium", "latte")

#returns

# def add_up(num1, num2): #defined a function with 2 parameters (3, 7)
#     return num1 + num2 # 3 + 7 then return the total to the function

# print(add_up(3, 7)) #prints the result


# global and local variables

# x = 1 #global variable

# def total_func():
#     y = 2 #local variable
#     z = 2 #local variable
#     global total #changes total from a local variable to a global variable
#     total = y + z
# total_func()

# print(total)
# #global variable = variable that exists in the entire codebase
# #local variable = variable that only exists within a function or specific section of code


# x = 1 #global variable

# def func_one():
#     x = 2 #local variable
#     print(x) #prints local variable
# func_one()

# print(x) #prints global variable
