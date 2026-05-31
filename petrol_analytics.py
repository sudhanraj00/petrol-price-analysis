import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("petrol_prices_india.csv")

print(df.head())
print(df.describe())

plt.figure(figsize=(12,6))
plt.plot(df["Year"], df["Petrol_Price"], marker="o")
plt.title("India Petrol Price Trend (2000-2026)")
plt.xlabel("Year")
plt.ylabel("Petrol Price (₹/Litre)")
plt.grid(True)
plt.show()

df["Growth_%"] = df["Petrol_Price"].pct_change() * 100

plt.figure(figsize=(12,6))
plt.bar(df["Year"], df["Growth_%"])
plt.title("Yearly Petrol Price Growth (%)")
plt.xlabel("Year")
plt.ylabel("Growth %")
plt.show()
