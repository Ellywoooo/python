import pandas as pd

# Using pyarrow backend to read parquet
df = pd.read_parquet("Sample_data_2.parquet")

# Display legnth of database
print(len(df))