import pandas as pd
import matplotlib.pyplot as plt
import re
import matplotlib.patches as mpatches

df = pd.read_csv("dataset_Facebook_modified.csv",usecols=["Page total likes","Lifetime People who have liked your Page and engaged with your post","like"])

page_total_likes=[]


lifetime_people_like=[]

post_like=[]

post_numbers=[]



for i in range(500):
    post_numbers.append(i)

for index,row in df.iterrows():
    if(row["Page total likes"]>0):
        page_total_likes.append(row["Page total likes"])


for index,row in df.iterrows():
    if(row["Lifetime People who have liked your Page and engaged with your post"]>0):
        lifetime_people_like.append(row["Lifetime People who have liked your Page and engaged with your post"])

for index,row in df.iterrows():
    post_like.append(row["like"])

for i in range(len(page_total_likes)-1):
    page_total_likes[i]=page_total_likes[i]-page_total_likes[i+1]

page_total_likes[len(page_total_likes)-1]=0


fig=plt.figure(figsize=(10,5))
fig.patch.set_facecolor("#1C212C")

ax= fig.add_subplot()
ax.patch.set_facecolor("#1C212C")



plt.plot(post_numbers,page_total_likes,color="#32579C")
plt.plot(post_numbers,lifetime_people_like,color="#302A6A")
plt.plot(post_numbers,post_like,color="#80C5A5")
plt.legend(['Page total likes','Lifetime People who have liked your\nPage and engaged with your post','Post Like'])
plt.xticks(color="white")
plt.yticks(color="white")
plt.title("Brand Loyalty = Page total likes compared with\n"
          "Lifetime people who have liked a page and engaged with a post compared with "
          "post likes",color="white")
plt.savefig("Brand Loyalty = Page total likes compared with Lifetime people who have liked a page and engaged with a post compared with post likes")

plt.show()
