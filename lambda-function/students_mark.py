marks={
    "anu":250,
    "vimal":450,
    "kavya":500,
    "abi":565,
    "sam":600,
    "arya":650
}

srt_students_mark=sorted(marks,key=lambda k:marks.get(k))

srt_students_mark=sorted(marks,key=lambda k:marks.get(k),reverse=True)   # desending 


print(srt_students_mark)