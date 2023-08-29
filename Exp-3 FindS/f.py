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