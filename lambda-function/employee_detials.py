employees=[
    ["sam",320000,5],
    ["karun",260000,3],
    ["ani",550000,8],
    ["rahul",40000,1],
    ["kavya",50000,2],
]

srt_emp_salary=sorted(employees,key=lambda lst:lst[1])

print(srt_emp_salary)

srt_emp_experience=sorted(employees,key=lambda emp:emp[2])

#print(srt_emp_experience)