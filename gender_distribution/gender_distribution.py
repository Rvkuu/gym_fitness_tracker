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

# 2. Gender Distribution
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Gender', palette='pastel')
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
