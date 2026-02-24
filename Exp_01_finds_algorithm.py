import csv

with open("weather_data.csv", "r", newline='') as file:
    data = list(csv.reader(file))

header = data[0]
data = data[1:]

# Take first training example
attributes = data[0][:-1]

# Initialize hypothesis with 0's
hypothesis = ['0'] * len(attributes)

# Process first row
if data[0][-1] == "Yes":
    hypothesis = attributes.copy()

# Process remaining rows
for row in data[1:]:
    attributes = row[:-1]
    target = row[-1]

    if target == "Yes":
        for i in range(len(hypothesis)):
            if hypothesis[i] != attributes[i]:
                hypothesis[i] = "?"

print("Header:", header)
print("Final Hypothesis:", hypothesis)