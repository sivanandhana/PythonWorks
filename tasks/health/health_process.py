file_path="tasks\\health\\mental_health_social_media_dataset.csv"

fr=open(file_path,"r")

import csv

reader=csv.DictReader(fr)

data=[row for row in reader]

print(len(data))

plat_form=[p.get("platform")for p in data]

print(plat_form)

platform_count={pc:plat_form.count(pc)for pc in plat_form}

print(platform_count)

you_tube_user=[y.get("person_name")for y in data if y.get("platform")=="YouTube"]

print(you_tube_user)


mental_state=[ms.get("mental_state")for ms in data ]

stressed_metal_count = mental_state.count("Stressed")

healthy_mental_count = mental_state.count("Healthy")

print(healthy_mental_count)

print(stressed_metal_count)

social_media_time_min = [int(st.get("social_media_time_min")) for st in data]

max_social_media_user= max(social_media_time_min)

print(max_social_media_user)

max_user_name=[u.get("person_name") for u in data if int(u.get("social_media_time_min"))==max_social_media_user]

print(max_user_name)


stress_level = [u.get("person_name")for u in data if int(u.get("stress_level"))<10]

print(stress_level)





