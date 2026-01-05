def bmi(heigth_in_cm,weight_in_kg):
    heigth_in_m= heigth_in_cm/100
    result=weight_in_kg/heigth_in_m**2
    return round(result)
print(bmi(156,50))
print(bmi(165,43))
print(bmi(188,85))
