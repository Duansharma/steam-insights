import pandas as pd

df = pd.read_csv("categories.csv")
df = df.sort_values(by=["app_id"], ascending=False)  # descending
df.to_csv("sortedfile.csv", index=False)

