
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("StudentsPerformance.csv")

# Explore
print(df.head())
print(df.shape)
print(df.info())

# ── Question 1: Average score in each subject ──
print("\n--- Average Scores ---")
print(df[["math score", "reading score", "writing score"]].mean())

# ── Question 2: Male vs Female performance ──
print("\n--- Average by Gender ---")
print(df.groupby("gender")[["math score", "reading score", "writing score"]].mean())

# ── Visualization: Boxplot Gender vs Math ──
sns.boxplot(x="gender", y="math score", data=df)
plt.title("Math Score by Gender")
plt.show()

# ── Question 3: Does test preparation help? ──
print("\n--- Test Preparation Impact ---")
print(df.groupby("test preparation course")[["math score", "reading score", "writing score"]].mean())

# ── Visualization ──
sns.boxplot(x="test preparation course", y="math score", data=df)
plt.title("Impact of Test Preparation on Math Score")
plt.show()

# ── Question 4: Performance by Race/Ethnicity ──
print("\n--- Average by Race/Ethnicity ---")
print(df.groupby("race/ethnicity")[["math score", "reading score", "writing score"]].mean())

# ── Visualization ──
plt.figure()
sns.barplot(x="race/ethnicity", y="math score", data=df)
plt.title("Math Score by Race/Ethnicity")
plt.show()

# ── Question 5: Top 10 Students ──
df["average"] = (df["math score"] + df["reading score"] + df["writing score"]) / 3

top10 = df.nlargest(10, "average")[["gender", "race/ethnicity", "math score", "reading score", "writing score", "average"]]
print("\n--- Top 10 Students ---")
print(top10)

# ── Visualization ──
plt.figure()
sns.histplot(df["average"], bins=20)
plt.title("Distribution of Average Scores")
plt.show()

# ── Correlation Heatmap ──
plt.figure()
corr = df[["math score", "reading score", "writing score"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Between Subjects")
plt.show()