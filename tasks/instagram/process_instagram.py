file_path="instagram\\Instagram_Analytics.csv"

fr=open(file_path,"r")

import csv

reader=csv.DictReader(fr)

data=[row for row in reader]

#print(len(data))

all_media=[m.get("media_type")for m in data]

# print(all_media)

like=[int(L.get("likes"))for L in data]

high_no_like=max(like)

most_liked_post=[L.get("post_id")for L in data if int(L.get("likes"))==high_no_like]

#print(most_liked_post)

comment=[int(c.get("comments"))for c in data]

high_comment=max(comment)

most_commented_post=[c.get("post_id")for c in data if int(c.get("comments"))==high_comment]

# print(most_commented_post)

gained=[int(c.get("followers_gained")) for c in data ]

maximum_followeer = max(gained)

followers_gained=[f.get("post_id")for f in data if int(f.get("followers_gained"))==maximum_followeer]

# print(followers_gained)



content_category=[cc.get("content_category")for cc in data]

# print(content_category)



content={c:content_category.count(c) for c in content_category}

# print(content)



