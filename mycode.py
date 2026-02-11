import pandas as pd
import os

data = {
    "date": ["2026-01-01","2026-01-02","2026-01-03","2026-01-04","2026-01-05","2026-01-06"],
    "product": ["apple","banana","orange","apple","banana","orange"],
    "units_sold": [10,5,8,7,12,6],
    "price_per_unit": [2,1,1.5,2,1,1.5]
}
df=pd.DataFrame(data)
df.loc[0,'units_sold']=100
df.loc[1,'units_sold']=200
df.loc[2,'units_sold']=300
df.loc[3,'units_sold']=400
df.loc[4,'units_sold']=500
df.loc[5,'units_sold']=600
df.loc[0,'product']='mango'
df.loc[1,'product']='grapes'
df.loc[2,'product']='papaya'
df.loc[3,'product']='apple'
df.loc[4,'product']='banana'
df.loc[5,'product']='orange'
df.loc[0,'price_per_unit']=20
df.loc[1,'price_per_unit']=10
df.loc[2,'price_per_unit']=15
df.loc[3,'price_per_unit']=20
df.loc[4,'price_per_unit']=10
df.loc[5,'price_per_unit']=15

data_dir='data'
os.makedirs(data_dir,exist_ok=True)
print(f'Folder created at {data_dir}')
file_path=os.path.join(data_dir,'sales.csv')
df.to_csv(file_path,index=False)
print(f"Data saved to {file_path}")

print("\nFirst 5 rows of the dataset:")
print(df.head())