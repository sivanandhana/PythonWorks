def emi(amount,tenure,rate):
    r=rate/(12*100)
    n=tenure*12
    result=(amount*r*(1+r)**n/(1+r)**n-1)
    return round(result)
print(emi(500000,6,8))