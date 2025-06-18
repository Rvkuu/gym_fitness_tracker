import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("cleaned_gym_members_exercise_tracking_synthetic_data.csv")

# Set up plot aesthetics
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

# ---------- PLOTS ----------

# Age Distribution
plt.figure()
sns.histplot(df['Age'], bins=20, kde=True, color='skyblue')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# Gender Count
plt.figure()
sns.countplot(data=df, x='Gender', palette='pastel')
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# Workout Type Distribution
plt.figure()
sns.countplot(data=df, x='Workout_Type', palette='Set2')
plt.title("Workout Type Distribution")
plt.xlabel("Workout Type")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# Calories Burned vs. Session Duration
plt.figure()
sns.scatterplot(data=df, x='Session_Duration (hours)', y='Calories_Burned',
                hue='Workout_Type', alpha=0.7)
plt.title("Calories Burned vs. Session Duration")
plt.xlabel("Session Duration (hours)")
plt.ylabel("Calories Burned")
plt.legend(title="Workout Type")
plt.show()

# BMI by Gender
plt.figure()
sns.boxplot(data=df, x='Gender', y='BMI', palette='coolwarm')
plt.title("BMI by Gender")
plt.xlabel("Gender")
plt.ylabel("BMI")
plt.show()

# Fat Percentage Across Age
plt.figure()
sns.lineplot(data=df.sort_values('Age'), x='Age', y='Fat_Percentage', color='purple')
plt.title("Fat Percentage Across Age")
plt.xlabel("Age")
plt.ylabel("Fat Percentage (%)")
plt.show()

# Heart Rate Comparison
plt.figure()
sns.boxplot(data=df[['Max_BPM', 'Avg_BPM', 'Resting_BPM']], palette='Set3')
plt.title("Heart Rate Statistics")
plt.ylabel("Beats Per Minute")
plt.show()

# Water Intake by Workout Type
plt.figure()
sns.violinplot(data=df, x='Workout_Type', y='Water_Intake (liters)', palette='Blues')
plt.title("Water Intake by Workout Type")
plt.xlabel("Workout Type")
plt.ylabel("Water Intake (liters)")
plt.xticks(rotation=45)
plt.show()

