import pandas as pd

# Using pyarrow or fastparquet backend
df = pd.read_parquet("Sample_data_2.parquet")

print(df)  # Display first few rows
