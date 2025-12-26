import pyodbc
import pandas as pd
import matplotlib.pyplot as plt

conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-FMNTILA\\SQLEXPRESS;"
    "Database=IPL2K25;"
    "Trusted_Connection=yes;"
)

query = """
SELECT TeamName, IndianPlayers, ForeignPlayers, TeamBudget
FROM IPL_2025_TEAMS
"""

df = pd.read_sql(query, conn)
print(df)

df.to_csv("IPL_2025_TEAMS.csv", index=False)
print("CSV file created")

plt.figure(figsize=(10,5))
plt.bar(df['TeamName'], df['TeamBudget'])
plt.xticks(rotation=45, ha='right')
plt.title("IPL 2025 Team Budgets")
plt.tight_layout()
plt.show()

x = range(len(df))
plt.figure(figsize=(12,6))
plt.bar(x, df['IndianPlayers'], width=0.4, label="Indian Players")
plt.bar([i+0.4 for i in x], df['ForeignPlayers'], width=0.4, label="Foreign Players")
plt.xticks([i+0.2 for i in x], df['TeamName'], rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.show()

top5 = df.sort_values(by="TeamBudget", ascending=False).head(5)
plt.figure(figsize=(8,5))
plt.bar(top5['TeamName'], top5['TeamBudget'])
plt.xticks(rotation=30, ha='right')
plt.title("Top 5 Teams by Budget")
plt.tight_layout()
plt.show()
