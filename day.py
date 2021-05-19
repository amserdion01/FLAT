mport matplotlib.pyplot as plt
import re
df = pd.read_csv("dataset_Facebook_modified.csv",usecols=["Post Weekday","Lifetime Post Total Reach"])

monday=[]
monday_contor=0
tuesday=[]
tuesday_contor=0
wednesday=[]
wednesday_contor=0
thursday=[]
thursday_contor=0
friday=[]
friday_contor=0
saturday=[]
saturday_contor=0
sunday=[]
sunday_contor=0

lifetime_post_total_reach=[]


for index, row in df.iterrows():
    pattern=re.compile(r'^Mo[a-z]*')
    match=pattern.findall(row["Post Weekday"])
    if len(match) > 0:
        monday.append(row["Lifetime Post Total Reach"])
        monday_contor+=1


for index, row in df.iterrows():
    pattern=re.compile(r'^Tu[a-z]*')
    match=pattern.findall(row["Post Weekday"])
    if len(match) > 0:
        tuesday.append(row["Lifetime Post Total Reach"])
        tuesday_contor+=1


for index, row in df.iterrows():
    pattern=re.compile(r'^We[a-z]*')
    match=pattern.findall(row["Post Weekday"])
    if len(match) > 0:
        wednesday.append(row["Lifetime Post Total Reach"])
        wednesday_contor+=1



for index, row in df.iterrows():
    pattern=re.compile(r'^Th[a-z]*')
    match=pattern.findall(row["Post Weekday"])
    if len(match) > 0:
        thursday.append(row["Lifetime Post Total Reach"])
        thursday_contor+=1



for index, row in df.iterrows():
    pattern=re.compile(r'^Fr[a-z]*')
    match=pattern.findall(row["Post Weekday"])
    if len(match) > 0:
        friday.append(row["Lifetime Post Total Reach"])
        friday_contor+=1



for index, row in df.iterrows():
    pattern=re.compile(r'^Sa[a-z]*')
    match=pattern.findall(row["Post Weekday"])
    if len(match) > 0:
        saturday.append(row["Lifetime Post Total Reach"])
        saturday_contor+=1




for index, row in df.iterrows():
    pattern=re.compile(r'^Su[a-z]*')
    match=pattern.findall(row["Post Weekday"])
    if len(match) > 0:
        sunday.append(row["Lifetime Post Total Reach"])
        sunday_contor+=1

xaxis=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
yaxis=[sum(monday)//monday_contor,sum(tuesday)//tuesday_contor,sum(wednesday)//wednesday_contor,sum(thursday)//thursday_contor,sum(friday)//friday_contor,sum(saturday)//saturday_contor,sum(sunday)//sunday_contor]




fig=plt.figure(figsize=(10,5))
fig.patch.set_facecolor("#1C212C")

ax= fig.add_subplot()
ax.patch.set_facecolor("#1C212C")
plt.bar(xaxis,yaxis,color={"#5176BA","#1C335C","#302A6A"})
plt.title("Lifetime Post Total Reach Measuread On Every Weekday",color="white")
plt.ylabel("Lifetime Post Total Reach",color="white")
plt.yticks([0,5000,10000,12500,15000,20000],color="white")
plt.xticks(color="white")
plt.savefig("Lifetime Post Total Reach Measuread On Every Weekday")
plt.show()
