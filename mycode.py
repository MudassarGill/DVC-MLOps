import pandas as pd
import os

data = {
    "date": ["2026-01-01","2026-01-02","2026-01-03","2026-01-04","2026-01-05","2026-01-06"],
    "product": ["apple","banana","orange","apple","banana","orange"],
    "units_sold": [10,5,8,7,12,6],
    "price_per_unit": [2,1,1.5,2,1,1.5]
}

df = pd.DataFrame(data)
data_dir='data'
os.makedirs(data_dir,exist_ok=True)
print(f'Folder created at {data_dir}')
file_path=os.path.join(data_dir,'sales.csv')
df.to_csv(file_path,index=False)
print(f"Data saved to {file_path}")

print("\nFirst 5 rows of the dataset:")
print(df.head())