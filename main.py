
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("finance_liquor_sales_2016_2019.csv")
df['percent_%'] = round((df['bottles_sold'] / df['bottles_sold'].sum())*100,2)
cn = df.groupby(['zip_code','category_name','store_name','percent_%'])['bottles_sold'].sum()
print(cn)

cn.to_csv('finance_liquor_aggregated.csv')






