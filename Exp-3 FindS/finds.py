import csv

# Read data from 'enjoysport.csv' and store it in list 'a'
with open('enjoysport.csv', 'r') as csvfile:
    a = [row for row in csv.reader(csvfile)]
    print(a)

print("\n The total number of training instances are: ", len(a))

num_attribute = len(a[0]) - 1

print("\n The initial hypothesis is:")
hypothesis = ['0'] * num_attribute
print(hypothesis)

# Training the hypothesis
for i in range(0, len(a)):
    if a[i][num_attribute] == 'yes':  # For each positive example only
        for j in range(0, num_attribute):
            if hypothesis[j] == '0' or hypothesis[j] == a[i][j]:
                hypothesis[j] = a[i][j]
            else:
                hypothesis[j] = '?'
        print("\n The hypothesis for the training instance {} is:".format(i + 1), hypothesis)

print("\n The Maximally specific hypothesis for the training instance is:")
print(hypothesis)
