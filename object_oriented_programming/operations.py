def operation(*args,**kwargs):

    # print(args)

    # print(kwargs)

    op=kwargs.get("key")

    if op=="max":

        return max(args)
    else:

        return min(args)

print(operation(10,20,30,40,key="max") )
print(operation(10,20,30,40,key="min")) 