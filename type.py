import pandas as pd
import matplotlib.pyplot as plt
import re

df = pd.read_csv("dataset_Facebook_modified.csv",usecols=["Type","Lifetime Engaged Users"])

photo=0
photo_c=0

video=0
video_c=0

link=0
link_c=0

status=0
status_c=0

lifetime_engaged_users=0

for index, row in df.iterrows():
    pattern = re.compile(r'^P[a-z]*')
    match = pattern.findall(row["Type"])
    if len(match) > 0:
        photo+=row["Lifetime Engaged Users"]
        photo_c+=1

for index, row in df.iterrows():
    pattern = re.compile(r'^V[a-z]*')
    match = pattern.findall(row["Type"])
    if len(match) > 0:
        video+=row["Lifetime Engaged Users"]
        video_c+=1

for index, row in df.iterrows():
    pattern = re.compile(r'^L[a-z]*')
    match = pattern.findall(row["Type"])
    if len(match) > 0:
        link+=row["Lifetime Engaged Users"]
        link_c+=1

for index, row in df.iterrows():
    pattern = re.compile(r'^S[a-z]*')
    match = pattern.findall(row["Type"])
    if len(match) > 0:
        status+=row["Lifetime Engaged Users"]
        status_c+=1



fig=plt.figure(figsize=(10,5))
fig.patch.set_facecolor("#1C212C")

ax= fig.add_subplot()
ax.patch.set_facecolor("#1C212C")

plt.bar(["Photo","Video","Link","Status"],[photo//photo_c,video//video_c,link//link_c,status//status_c])
plt.xticks(color="white")
plt.yticks(color="white")
plt.ylabel("Lifetime Engaged Users",color="white")
plt.title("Impact on Lifetime Engaged Users based on post type",color="white")
plt.savefig("Impact on Lifetime Engaged Users based  on post type")

plt.show()
