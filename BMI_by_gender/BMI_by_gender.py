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

# 5. BMI by Gender
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Gender', y='BMI', palette='coolwarm')
plt.title("BMI by Gender")
plt.xlabel("Gender")
plt.ylabel("BMI")
plt.tight_layout()
plt.show()
