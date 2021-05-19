import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("dataset_Facebook.csv")

#changing the values at specific place in the dataset
df["Category"]=df["Category"].replace(1,"Action")
df["Category"]=df["Category"].replace(2,"Product")
df["Category"]=df["Category"].replace(3,"Inspiration")


df["Post Month"]=df["Post Month"].replace(1,"January")
df["Post Month"]=df["Post Month"].replace(2,"February")
df["Post Month"]=df["Post Month"].replace(3,"March")
df["Post Month"]=df["Post Month"].replace(4,"April")
df["Post Month"]=df["Post Month"].replace(5,"May")
df["Post Month"]=df["Post Month"].replace(6,"June")
df["Post Month"]=df["Post Month"].replace(7,"July")
df["Post Month"]=df["Post Month"].replace(8,"August")
df["Post Month"]=df["Post Month"].replace(9,"September")
df["Post Month"]=df["Post Month"].replace(10,"October")
df["Post Month"]=df["Post Month"].replace(11,"November")
df["Post Month"]=df["Post Month"].replace(12,"December")

df["Post Weekday"]=df["Post Weekday"].replace(1,"Sunday")
df["Post Weekday"]=df["Post Weekday"].replace(2,"Monday")
df["Post Weekday"]=df["Post Weekday"].replace(3,"Tuesday")
df["Post Weekday"]=df["Post Weekday"].replace(4,"Wednesday")
df["Post Weekday"]=df["Post Weekday"].replace(5,"Thursday")
df["Post Weekday"]=df["Post Weekday"].replace(6,"Friday")
df["Post Weekday"]=df["Post Weekday"].replace(7,"Saturday")


df["Paid"]=df["Paid"].replace(0,"No")
df["Paid"]=df["Paid"].replace(1,"Yes")

df.to_csv("dataset_Facebook_modified.csv",index=False)

