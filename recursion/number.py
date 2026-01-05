# def display_numbers(limit):

#     if limit==1:

#         return 1
    
#     print(limit)

#     return display_numbers(limit-1)

# display_numbers(10)

def display_number(limit):

    if limit==0:

        return 
    
    print(limit)

    return display_number(limit-1)

display_number(15)