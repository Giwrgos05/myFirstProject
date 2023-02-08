
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('finance_liquor_aggregated.csv')
print(df.info())

x=df['zip_code']
y=df['bottles_sold']
colors = np.random.randint(68, size=(68))

plt.scatter(x, y, c=colors, cmap='nipy_spectral')

plt.title("Bottles Sold")
plt.xlabel("Zip Code")
plt.ylabel("Bottles Sold")


plt.show()



