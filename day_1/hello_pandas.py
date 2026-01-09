import pandas as pd

data = {
    "name": ["Ali", "Ayşe", "Mehmet"],
    "age": [25, 30, 28],
    "department": ["HR", "IT", "Finance"]
}

df = pd.DataFrame(data)

print(df)
