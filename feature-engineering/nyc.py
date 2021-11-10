import pandas as pd

df = pd.read_csv("nyc.csv")

print(df.shape) # prints the dimensions

print(df.describe())

min, max = df.price.quantile([0.001, 0.999])

print(min,max)

outliers = df[(df.price > max) | (df.price < min)]
datapoints = df[(df.price < max) & (df.price > min)]

print(outliers.shape)
print(datapoints.describe())
print(datapoints.columns.values)
print(datapoints.iloc[5])