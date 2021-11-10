import pandas as pd

df = pd.read_csv("realEstate.csv")

print(df.shape) # prints the dimensions

print(df.describe())

min, max = df.price_per_sqft.quantile([0.001, 0.999])

outliers = df[(df.price_per_sqft > max) | (df.price_per_sqft < min)]
datapoints = df[(df.price_per_sqft < max) & (df.price_per_sqft > min)]

print(outliers.shape)
print(datapoints.shape)