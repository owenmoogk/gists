import pandas as pd

df = pd.read_csv("myData.csv")
# print(df)

maxThreshold = df["height"].quantile(0.95)
minThreshold = df["height"].quantile(0.05)

print(minThreshold, maxThreshold)

# remove outliers
df = df[(df["height"] < maxThreshold) & (df["height"] > minThreshold)]
print(df)