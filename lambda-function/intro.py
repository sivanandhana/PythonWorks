"""
lambda =  anonymous functions with single expression

"""

add_numbers=lambda n1,n2:n1+n2

print(add_numbers(500,200))

square=lambda n:n**2

print(square(5))

cube=lambda n:n**3

print(cube(5))

odd_even=lambda n:"odd" if n%2!=0 else "even"

print(odd_even(5))

is_negative=lambda n:True if n<0 else False

print(is_negative(-1))

is_century_year=lambda n:True if n%100==0 else False

print(is_century_year(2020))