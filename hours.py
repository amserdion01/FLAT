import pandas as pd
import matplotlib.pyplot as plt
import re

df = pd.read_csv("dataset_Facebook_modified.csv",usecols=["Post Hour","Lifetime Engaged Users"])

interval_one=0
one_counter=0
interval_two=0
two_counter=0
interval_three=0
three_counter=0
interval_four=0
four_counter=0
interval_five=0
five_counter=0
interval_six=0
six_counter=0

lifetime_engaged_users=0

for index, row in df.iterrows():
    if row["Post Hour"] >=1 and row["Post Hour"] <=4:
        interval_one += row["Lifetime Engaged Users"]
        one_counter+=1
    lifetime_engaged_users+=row["Lifetime Engaged Users"]

for index, row in df.iterrows():
    if row["Post Hour"] >=5 and row["Post Hour"] <=8:
        interval_two += row["Lifetime Engaged Users"]
        two_counter+=1

for index, row in df.iterrows():
    if row["Post Hour"] >=9 and row["Post Hour"] <=12:
        interval_three += row["Lifetime Engaged Users"]
        three_counter+=1

for index, row in df.iterrows():
    if row["Post Hour"] >=13 and row["Post Hour"] <=16:
        interval_four += row["Lifetime Engaged Users"]
        four_counter+=1

for index, row in df.iterrows():
    if row["Post Hour"] >=17 and row["Post Hour"] <=20:
        interval_five += row["Lifetime Engaged Users"]
        five_counter+=1

for index, row in df.iterrows():
    if row["Post Hour"] >=21 and row["Post Hour"] <=24:
        interval_six += row["Lifetime Engaged Users"]
        six_counter+=1


fig=plt.figure(figsize=(10,5))
fig.patch.set_facecolor("#1C212C")

ax= fig.add_subplot()
ax.patch.set_facecolor("#1C212C")

yaxis=[interval_one//one_counter,interval_two//two_counter,interval_three//three_counter,interval_four//four_counter,interval_five//five_counter,interval_six//six_counter]

bars=plt.bar(["Hour 01-04","Hour 05-08","Hour 09-12","Hour 13-16","Hour 17-20","Hour 21-24"],yaxis,color=["#5176BA","#1C335C","#302A6A"])
plt.yticks(color="white")
plt.title("Impact of post on different hours interval",color="white")
plt.ylabel(" Mean of Lifetime Engaged Users ",color="white")
plt.xticks(color="white")
plt.savefig("Impact of post on different hours interval")
plt.show()
# plt.savefig("Impact of different category posts to the Lifetime Engaged Users")
