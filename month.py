import pandas as pd
import matplotlib.pyplot as plt
import re

df = pd.read_csv("dataset_Facebook_modified.csv",usecols=["Post Month","Lifetime Engaged Users"])

jan=0
jan_c=0

feb=0
feb_c=0

mar=0
mar_c=0

apr=0
apr_c=0

may=0
may_c=0

jun=0
jun_c=0

jul=0
jul_c=0

aug=0
aug_c=0

sep=0
sep_c=0

oct=0
oct_c=0

nov=0
nov_c=0

dec=0
dec_c=0

lifetime_engaged_users=0

for index, row in df.iterrows():
    pattern = re.compile(r'^Jan[a-z]*')
    match = pattern.findall(row["Post Month"])
    if len(match) > 0:
        jan+= row["Lifetime Engaged Users"]
        jan_c+=1

for index, row in df.iterrows():
    pattern = re.compile(r'^Feb[a-z]*')
    match = pattern.findall(row["Post Month"])
    if len(match) > 0:
        feb+= row["Lifetime Engaged Users"]
        feb_c+=1

for index, row in df.iterrows():
    pattern = re.compile(r'^Mar[a-z]*')
    match = pattern.findall(row["Post Month"])
    if len(match) > 0:
        mar+= row["Lifetime Engaged Users"]
        mar_c+=1

for index, row in df.iterrows():
    pattern = re.compile(r'^Apr[a-z]*')
    match = pattern.findall(row["Post Month"])
    if len(match) > 0:
        apr+= row["Lifetime Engaged Users"]
        apr_c+=1

for index, row in df.iterrows():
    pattern = re.compile(r'^May[a-z]*')
    match = pattern.findall(row["Post Month"])
    if len(match) > 0:
        may+= row["Lifetime Engaged Users"]
        may_c+=1

for index, row in df.iterrows():
    pattern = re.compile(r'^Jun[a-z]*')
    match = pattern.findall(row["Post Month"])
    if len(match) > 0:
        jun+= row["Lifetime Engaged Users"]
        jun_c+=1

for index, row in df.iterrows():
    pattern = re.compile(r'^Jul[a-z]*')
    match = pattern.findall(row["Post Month"])
    if len(match) > 0:
        jul+= row["Lifetime Engaged Users"]
        jul_c+=1

for index, row in df.iterrows():
    pattern = re.compile(r'^Aug[a-z]*')
    match = pattern.findall(row["Post Month"])
    if len(match) > 0:
        aug+= row["Lifetime Engaged Users"]
        aug_c+=1

for index, row in df.iterrows():
    pattern = re.compile(r'^Sep[a-z]*')
    match = pattern.findall(row["Post Month"])
    if len(match) > 0:
        sep+= row["Lifetime Engaged Users"]
        sep_c+=1

for index, row in df.iterrows():
    pattern = re.compile(r'^Oct[a-z]*')
    match = pattern.findall(row["Post Month"])
    if len(match) > 0:
        oct+= row["Lifetime Engaged Users"]
        oct_c+=1

for index, row in df.iterrows():
    pattern = re.compile(r'^Nov[a-z]*')
    match = pattern.findall(row["Post Month"])
    if len(match) > 0:
        nov+= row["Lifetime Engaged Users"]
        nov_c+=1

for index, row in df.iterrows():
    pattern = re.compile(r'^Dec[a-z]*')
    match = pattern.findall(row["Post Month"])
    if len(match) > 0:
        dec+= row["Lifetime Engaged Users"]
        dec_c+=1


fig=plt.figure(figsize=(10,5))
fig.patch.set_facecolor("#1C212C")

ax= fig.add_subplot()
ax.patch.set_facecolor("#1C212C")

yaxis=[jan//jan_c,feb//feb_c,mar//mar_c,apr//apr_c,may//may_c,jun//jun_c,jul//jul_c,aug//aug_c,sep//sep_c,oct//oct_c,nov//nov_c,dec//dec_c]

bars=plt.bar(["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],yaxis,color=["#5176BA","#1C335C","#302A6A"])
plt.yticks(color="white")
plt.title("Impact of posts on different months",color="white")
plt.ylabel(" Mean of Lifetime Engaged Users ",color="white")
plt.xticks(color="white")
plt.savefig("Impact of posts on different months")
plt.show()
