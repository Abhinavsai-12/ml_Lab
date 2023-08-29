import csv

with open("enjoysport.csv") as f:
    csv_file = csv.reader(f)
    data = list(csv_file)

print(data)
print("--------------------")

s = data[1][:-1]  # Extracting one row or instance or record
g = [['?' for i in range(len(s))] for j in range(len(s))]

print(s)
print("--------------------")
print(g)
print("--------------------")

for i in data:
    if i[-1] == "yes":  # For each positive training record or instance
        for j in range(len(s)):
            if i[j] != s[j]:
                s[j] = '?'
    else:  # For each negative training record or example
        for j in range(len(s)):
            if i[j] != s[j]:
                g[j][j] = '?'

    print("\nSteps of Candidate Elimination Algorithm", data.index(i) + 1)
    print(s)
    print(g)

gh = []
for i in g:
    temp = []
    for j in i:
        if j != '?':
            temp.append(j)
    if temp:
        gh.append(temp)

print("\nFinal specific hypothesis:\n", s)
print("\nFinal general hypothesis:\n", gh)
