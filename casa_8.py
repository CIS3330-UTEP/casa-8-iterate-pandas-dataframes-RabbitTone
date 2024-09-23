import pandas as pd

df = pd.read_csv('big-mac-full-index.csv')

print("\nIterating over rows using iterrows() method :\n")

# Using iterrows() method
for index, row in df.iterrows():
    print(row["date"],row["iso_a3"],row["currency_code"],row["name"])

print("\nIterating over rows using apply() method :\n")

# Using apply() method
print(df.apply(lambda row: row['name'] +  " "  + 
               str(row['local_price']) +  " "  + 
               str(row['dollar_ex']) +  " "  + 
               str(row['dollar_price']), axis=1))