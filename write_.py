import csv
import random

data = []

for i in range(100):
    data.append({
        "experience": round(random.random() * 10, 2),
        "Age": random.randint(18, 75),
        "Salary": random.randint(10_000, 200_000)
    })


with open("my_salary.csv", "w") as file:
    fieldnames = ["experience", "Age", "Salary"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for line in data:
        writer.writerow(line)