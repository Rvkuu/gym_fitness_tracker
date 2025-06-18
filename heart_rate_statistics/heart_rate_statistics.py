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

# 7. Heart Rate Statistics
plt.figure(figsize=(8, 6))
sns.boxplot(data=df[['Max_BPM', 'Avg_BPM', 'Resting_BPM']], palette='Set3')
plt.title("Heart Rate Statistics")
plt.ylabel("Beats Per Minute")
plt.tight_layout()
plt.show()
