# Re-import required libraries and re-load the dataset due to session reset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reload the dataset
file_path = "/mnt/data/cleaned_gym_members_exercise_tracking_synthetic_data.csv"
df = pd.read_csv(file_path)

# Set up plot aesthetics
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

# 1. Age Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], bins=20, kde=True, color='skyblue')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

