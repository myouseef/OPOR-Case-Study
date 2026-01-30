import pandas as pd

# Load sample patient data
df = pd.read_csv('../data/patients_before.csv')

# Deduplicate based on National ID
df_merged = df.drop_duplicates(subset=['National_ID'])

# Save the cleaned data
df_merged.to_csv('../data/patients_after.csv', index=False)

print("Deduplication complete!")
print("Records reduced from", len(df), "to", len(df_merged))