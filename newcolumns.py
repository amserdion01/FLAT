import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("dataset_Facebook_modified.csv")


#adding new columns to the data set
df["People who are not interested in the post"]= df["Lifetime Post Total Reach"] - df["Lifetime Engaged Users"]
df["New Viewers"] = df["Lifetime Post Total Reach"] - df["Lifetime Post reach by people who like your Page"]


df.to_csv("dataset_Facebook_modified.csv")
