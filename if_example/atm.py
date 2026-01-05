db_pin = 1234
db_balance = 6000

pin =int(input("enter a pin : "))
if(pin == db_pin):
    balance=int(input("enter a balance : "))
    if(balance==db_balance):
        print("sufficient balance")
    else:
        print("insufficient balance")
else:
    print("invalid pin ")
