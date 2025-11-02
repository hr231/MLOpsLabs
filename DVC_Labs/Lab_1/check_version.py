import pandas as pd

df = pd.read_csv('data/CC_GENERAL.csv')
print(f'Dataset has {len(df)} customers')
print(f'File size: {df.memory_usage(deep=True).sum() / 1024:.2f} KB')
print(f'Last 5 customer IDs:')
for cust_id in df.tail(5)['CUST_ID'].tolist():
    print(f'  - {cust_id}')

