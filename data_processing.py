import pandas as pd

# Load incident data
df = pd.read_csv("incident_data.csv")

# Data Cleaning & Transformation
df.fillna("Unknown", inplace=True)
df["Resolution_Status"] = df["Status"].apply(lambda x: "Closed" if x == "Resolved" else "Open")

# Save processed data
df.to_csv("processed_incident_data.csv", index=False)

print("Data processing completed successfully.")
