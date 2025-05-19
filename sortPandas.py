# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pandas",
# ]
# ///
# This script demonstrates how to create a DataFrame using the pandas library in Python.

import pandas as pd

df2 = pd.read_json("poductCatalog.json")



print(df2)
df_filtered = df2[df2["price"] >= 85.10]
df_sorted = df_filtered.sort_values(by=["category","price","name"], ascending=[True, False, True])
print(df_sorted)
sorted_json = df_sorted.to_json(orient='records', indent=2)

# Optionally write to a file
with open("sorted_data.json", "w") as f:
    f.write(sorted_json)