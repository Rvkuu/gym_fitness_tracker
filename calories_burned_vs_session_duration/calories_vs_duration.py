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

# 4. Calories Burned vs. Session Duration
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x='Session_Duration (hours)', y='Calories_Burned',
                hue='Workout_Type', alpha=0.7)
plt.title("Calories Burned vs. Session Duration")
plt.xlabel("Session Duration (hours)")
plt.ylabel("Calories Burned")
plt.legend(title="Workout Type")
plt.tight_layout()
plt.show()
