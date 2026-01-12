import pandas as pd

df = pd.read_csv("categories.csv")
df = df.sort_values(by=['app_id'], decending=True)
df.to_csv("sortedfile.csv", index=False)

