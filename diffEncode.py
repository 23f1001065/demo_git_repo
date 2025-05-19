import pandas as pd
symbols = {'Ž', 'ž', '€'}


df1 = pd.read_csv("data1.csv", encoding="cp1252")
df2 = pd.read_csv("data2.csv", encoding="utf-8")
df3 = pd.read_csv("data3.txt", encoding="utf-16", sep="\t")

# Filter and sum
total = 0
print(df1)
print(df2)
print(df3)
for df in [df1, df2, df3]:
    # Ensure 'value' is numeric
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    # Filter by symbol
    match = df[df['symbol'].isin(symbols)]
    total += match['value'].sum()

print("Total sum for symbols Ž, ž, or €:", total)