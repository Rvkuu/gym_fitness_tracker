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

# 8. Water Intake by Workout Type
plt.figure(figsize=(10, 6))
sns.violinplot(data=df, x='Workout_Type', y='Water_Intake (liters)', palette='Blues')
plt.title("Water Intake by Workout Type")
plt.xlabel("Workout Type")
plt.ylabel("Water Intake (liters)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
