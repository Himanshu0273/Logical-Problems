import matplotlib.pyplot as plt
import csv

countries = []
medals = []

with open(r"data.csv", 'r') as input_file:
    reader = csv.DictReader(input_file)
    for row in reader:
        countries.append(row["country"])
        medals.append(int(row["medals"]))  # Convert to int

plt.figure(figsize=(8, 8))
plt.pie(medals, labels=countries, autopct='%1.1f%%')
plt.title("Gold Medals for Each Country")
plt.axis("equal")
plt.show()
