import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------
# Create DataFrame (from SQL data)
# ----------------------------
data = {
    "StudentID": [1,2,3,4,5,6,7,8],
    "StudentName": ["Ravi","Sita","Kiran","Anu","Rahul","Priya","Suresh","Meena"],
    "Age": [15,14,15,13,14,15,13,14],
    "Class": ["10th","9th","10th","8th","9th","10th","8th","9th"],
    "Maths": [78,88,65,92,55,85,72,90],
    "Physics": [82,90,70,95,60,88,75,92],
    "Chemistry": [75,85,68,91,58,90,70,94],
    "TotalMarks": [235,263,203,278,173,263,217,276]
}

df = pd.DataFrame(data)

# ----------------------------
# Display Data
# ----------------------------
print("\nStudent Data:")
print(df)

# ----------------------------
# 1. Average Marks by Class
# ----------------------------
avg_class = df.groupby("Class")["TotalMarks"].mean()

plt.figure()
avg_class.plot(kind="bar")
plt.title("Average Marks by Class")
plt.xlabel("Class")
plt.ylabel("Average Marks")
plt.show()

# ----------------------------
# 2. Student Count by Age
# ----------------------------
age_count = df["Age"].value_counts().sort_index()

plt.figure()
age_count.plot(kind="bar")
plt.title("Student Count by Age")
plt.xlabel("Age")
plt.ylabel("Number of Students")
plt.show()

# ----------------------------
# 3. Top Scorers
# ----------------------------
top_students = df.sort_values(by="TotalMarks", ascending=False).head(3)

plt.figure()
plt.bar(top_students["StudentName"], top_students["TotalMarks"])
plt.title("Top 3 Students by Total Marks")
plt.xlabel("Student Name")
plt.ylabel("Total Marks")
plt.show()
