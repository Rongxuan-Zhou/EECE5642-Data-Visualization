import pandas as pd

# 读取数据
df = pd.read_excel('../data/data-1.xlsx')

# 打印数据信息
print("DataFrame Info:")
print(df.info())
print("\nFirst few rows of data:")
print(df.head())