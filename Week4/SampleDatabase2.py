import pandas as pd

# Using pyarrow backend
df = pd.read_parquet("Sample_data_2.parquet")

# Display all  
print(df)