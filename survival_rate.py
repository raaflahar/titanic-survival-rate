import pandas as pd
import matplotlib.pyplot as plt

# Reading Data

titanic_df = pd.read_excel("titanic.xlsx", sheet_name="titanic")

# Survival Rate

survival_counts = titanic_df["Survived"].value_counts()

print(survival_counts)

labels = ["Deceased", "Survived"]
sizes = survival_counts.values
colors = ["skyblue", "pink"]
explode = (0.1, 0)

# Survival Rate by Gender

survival_by_gender = titanic_df.groupby("Sex")["Survived"].mean()

print(survival_by_gender)

# Visualize Survival Rate

plt.figure(figsize=(8,5))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode)
plt.title("Survival Rate")

plt.figure(figsize=(8, 5))
survival_counts.plot(kind='bar', color=['skyblue', 'pink'], edgecolor='black')
plt.title("Survival Rate", fontsize=14)
plt.ylabel("Rate", fontsize=12)
plt.xticks(ticks=[0, 1], labels=labels, rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Visualize Survival Rate by Gender
plt.figure(figsize=(8, 5))
survival_by_gender.plot(kind='bar', color=['pink'], edgecolor='black')
plt.title("Survival Rate by Gender", fontsize=14)
plt.ylabel("Survival Rate", fontsize=12)
plt.xlabel("Gender", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.show()

