import pandas as pd
import matplotlib.pyplot as plt
import re
df = pd.read_csv("dataset_Facebook_modified.csv",usecols=["Category","Lifetime Engaged Users"])

print(df)

product_mean=0
action_mean=0
inspiration_mean=0


total_lifetime_engaged_users = 0
counter = 0

for index, row in df.iterrows():
    pattern=re.compile(r'^P[a-z]*')
    match=pattern.findall(row["Category"])
    if len(match) > 0:
        total_lifetime_engaged_users += row["Lifetime Engaged Users"]
        counter += 1
product_mean=(total_lifetime_engaged_users//counter)

total_lifetime_engaged_users = 0
counter = 0
for index, row in df.iterrows():
    pattern=re.compile(r'^A[a-z]*')
    match=pattern.findall(row["Category"])
    if len(match) > 0:
        total_lifetime_engaged_users += row["Lifetime Engaged Users"]
        counter += 1
action_mean=(total_lifetime_engaged_users//counter)


total_lifetime_engaged_users = 0
counter = 0
for index, row in df.iterrows():
    pattern=re.compile(r'^I[a-z]*')
    match=pattern.findall(row["Category"])
    if len(match) > 0:
        total_lifetime_engaged_users += row["Lifetime Engaged Users"]
        counter += 1
inspiration_mean=(total_lifetime_engaged_users//counter)


fig=plt.figure(figsize=(10,5))
fig.patch.set_facecolor("#1C212C")

ax= fig.add_subplot()
ax.patch.set_facecolor("#1C212C")

bars=plt.bar(['Product Post Impact','Action Post Impact','Inspiration Post Impact'],[product_mean,action_mean,inspiration_mean],color=["#5176BA","#302A6A","#32579C"])
plt.yticks([0,250,500,750,1000,1250,1500,1750],color="white")
plt.xticks(color="white")
plt.title("Impact of different category posts to the Lifetime Engaged Users",color="white")
plt.ylabel(" Mean of Lifetime Engaged Users ",color="white")
plt.savefig("Impact of different category posts to the Lifetime Engaged Users")
plt.show()
