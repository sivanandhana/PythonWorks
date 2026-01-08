from json import load

file_path ="json_works\\oscar\\oscar-best-picture-award-winners.json"

fr = open(file_path,"r",encoding="utf-8")

data = load(fr)

print(len(data))

movie_title = [mt.get("name")for mt in data]

# print(movie_title)

# oscar_movie = [m.get("name"),m.get("year") for m in data ]
# print(oscar_movie)

movie_released =[mr.get("name")for mr in data if int(mr.get("released_year"))<2000]

# print(movie_released)

greatest_runtime =[r.get("name") for r in data if r.get("duration")>"150"]

# print(greatest_runtime)

# Dic_name =[dirc for dirc in data if dirc.get("directors").startswith("s")]

# print(Dic_name)

total_oscar_movies =[om.get("oscar") for om in data ]

# print(total_oscar_movies)

less_runtime = [rt.get("name") for rt in data if rt.get("duration")<"90 min"]



print(less_runtime)

