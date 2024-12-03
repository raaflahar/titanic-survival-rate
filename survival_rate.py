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

survival_by_gender = titanic_df.groupby("Sex")["Survived"].mean() * 100
survival_by_pclass = titanic_df.groupby("Pclass")["Survived"].mean() * 100

print(survival_by_gender)
print(survival_by_pclass)

# Visualize Survival Rate
plt.figure(figsize=(8,5))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode)
plt.title("Survival Rate")

# Visualize Survival Rate by Class
plt.figure(figsize=(8, 5))
bars = plt.bar(
    survival_by_pclass.index,  
    survival_by_pclass.values,  
    color=['gold', 'silver', 'brown'],  
    edgecolor='black'
)

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,  
        bar.get_height() - 5,              
        f"{bar.get_height():.1f}%",        
        ha='center', va='center', fontsize=12, color='black'
    )

plt.title("Survival Rate by Passenger Class", fontsize=14)
plt.ylabel("Survival Rate (%)", fontsize=12)
plt.xlabel("Pclass", fontsize=12)
plt.xticks(ticks=[1, 2, 3], labels=["Class 1", "Class 2", "Class 3"], rotation=0)
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(
    bars,
    ["Class 1 (Gold)", "Class 2 (Silver)", "Class 3 (Bronze)"], 
    loc='upper left',
    fontsize=10
)

# Visualize Survival Rate by Gender
plt.figure(figsize=(8, 5))
survival_by_gender.plot(kind='bar', color=['pink'], edgecolor='black')
plt.title("Survival Rate by Gender", fontsize=14)
plt.ylabel("Survival Rate (%)", fontsize=12)
plt.xlabel("Gender", fontsize=12)
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.show()

