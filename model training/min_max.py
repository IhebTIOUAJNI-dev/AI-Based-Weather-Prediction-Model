import pandas as pd

# Load the CSV file
df = pd.read_csv("model training/data.csv")

# checks the highest and lowest value of each column in the dataset
for column in df.columns:
    if df[column].dtype in ['int64', 'float64']:  
        max_value = df[column].max()
        min_value = df[column].min()
        print(f"{column}:")
        print(f"Highest value: {max_value}")
        print(f"Lowest value: {min_value}")