# Fragmented Patient Records: A Case Study

## Introduction

In modern healthcare, patient data is often fragmented across multiple systems. This case study demonstrates how fragmented records impact AI performance and clinical decisions, and how **One Person, One Record (OPOR)** can solve this problem.

## Scenario

A patient visiting a hospital had three separate records across different departments: Lab, Pharmacy, and Radiology.

- Lab recommended repeated blood tests.
- Pharmacy recommended conflicting medications.
- Allergy warning from Radiology was ignored.

AI decision support failed because it could not reconcile the fragmented data.

AI decision support failed because it could not reconcile the fragmented data.

![Fragmented Records](images/record_merged1.png)

## Challenges

- Duplicate patient records across departments
- Conflicting clinical information
- Reduced trust in AI recommendations
- Increased risk of medical errors

## Solution Approach

1. Implemented **One Person, One Record (OPOR)**.
2. Used automated **data matching and deduplication scripts** to unify patient records.
3. Verified AI recommendations against the unified dataset.

## Example Python Code

```python
import pandas as pd

# Load sample patient data
df = pd.read_csv('data/patients_before.csv')

# Simple deduplication based on National ID
df_merged = df.drop_duplicates(subset=['National_ID'])

# Save merged dataset
df_merged.to_csv('data/patients_after.csv', index=False)
print("Deduplication complete. Records reduced from", len(df), "to", len(df_merged))
```

## Results

- Consolidated patient records into a single source of truth.
- AI recommendations became accurate and actionable.
- Reduced repeated tests and medication errors.

## Lessons Learned

- OPOR is essential for AI in healthcare.
- Even simple deduplication scripts can significantly improve clinical decision-making.
- Maintaining a clean, unified dataset is critical before deploying AI tools.

## Conclusion

Fragmented patient data undermines AI and clinical decisions. Implementing OPOR, supported by automated tools, is key to safe, intelligent healthcare.
