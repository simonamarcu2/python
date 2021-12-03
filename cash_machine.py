
cash_v = [100.00,50.00,20.00,10.00]	#array containing all possible values

# pin = input("\n Type your PIN: \n")
# withdrawal = input("\n What amound would you like to withdraw? \n")
# amount = 300
# withdrawal(amount):

# print(f"Withdrawing £{withdrawal} ...")

def account():
    print ("Hello, welcome to Bank of Python!")
    print ("Please enter your account pin number")
    account = input("insert PIN: \n")
    account = (1234)
    answer = input(withdraw)

account()

def balance():
    print ("would you like to see your account balance?")
    see = input("Enter Y or N: ")
    if (see == "Y") or (see == "y"):
        balance = int(500)
    print ("Current balance: £" + str(balance))

balance()

def withdraw(): 
    if answer == "w":
        print ("How much would you like to withdraw?")
        withdraw = input("Enter amount to withdraw: ")
        withdraw = int(withdraw)

        currentbalance = withdraw - balance
        print ("Withdrew: $" + str(withdraw))
        print ("Current Balance: $" + str(currentbalance))

withdraw()        


# def new_func(cash_v):
#   def Main():
#     while True: #main loop, interrupt with keyboard to exit
#       try:
#         withdrawal = float(input())
#         if withdrawal <= 0:		#check negative values
#           msg = "Invalid Value"
#         else:
#           return_array = []
#           while (withdrawal >= min(cash_v)):
#             for i in range(len(cash_v)): 
#               if withdrawal >= cash_v[i]:
#                 withdrawal = withdrawal - cash_v[i]
#                 return_array.append(cash_v[i])
#                 break
#           msg = return_array
#           if withdrawal > 0: # check if rest exists
#             msg = "Error Value"
#       except ValueError:
#         msg = "Error no value"
#       print(msg)
#   return Main

# Main = new_func(cash_v)


# if __name__ == '__main__': 
#   Main() 
