import csv

young = []
adult = []

with open("Salary_Data.csv", "r") as file:
    f_ = csv.DictReader(file)
    for line in f_:
        if float(line["Age"]) > 30:
            adult.append(int(line["Salary"]))
        else:
            young.append(int(line["Salary"]))

print(sum(young)/len(young))
print(sum(adult)/len(adult))
        