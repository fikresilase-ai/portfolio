import pandas as pd

# Load sample data
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25,30, 35],
"City": ["Addis Ababa", "Lagos", "Nairobi"]
}
df = pd.DataFrame(data)

print("Data Summary:")
print(df.describe())