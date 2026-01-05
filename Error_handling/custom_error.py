age = int(input("enter your age : "))

if age <18:

    raise Exception("Invalid age")   # keyword for throw custom_eror
else:
    print("eligible for vote")