import pandas as pd
data = pd.read_csv("/Users/andrestavera/Documents/GitHub/retoAnalitica/avocado.csv")

print("data", data.head)
print(data.iloc[15,2])


print(data.sort_values(by="AveragePrice"))

rows= len(data.axes[0])
cols= len(data.axes[1])
print(f"rows: {rows}\ncols {cols}")


print(data["AveragePrice"].max())

print(data["AveragePrice"].min())
