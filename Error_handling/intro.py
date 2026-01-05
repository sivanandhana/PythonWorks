""" 
ERROR HANDLING
---------------

1. SYNTAX ERROR
2. LOGICAL ERROR
3. RUNTIME ERROR  (ZeroDivisionError ,FileNotFound,KeyError,ValueError,IndexError)


block
******

try :
    doubtful code

except :
    
        error hadling code
finally :

        cleanup process


keywords
-----------

* raise (custom error)
* asserts (debug)

"""
num1= int(input("Enter a numer : "))
num2= int(input("Enter a numer : "))

try:

    result=num1/num2

    print(result)

except Exception as e:

    print(e)

    
print("file operation")

print("database commit")