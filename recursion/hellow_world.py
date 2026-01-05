"""

a function calling by its self is called recursion
with a base condition

"""

def display_hello_world(limit):

    if limit==0:

        return
    
    print("hello world")

    return display_hello_world(limit-1)


display_hello_world(5)

