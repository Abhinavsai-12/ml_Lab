import csv

def read_data(csv_filename):
    with open(csv_filename, 'r') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',')
        headers = next(datareader)
        metadata = []
        traindata = []
        for name in headers:
            metadata.append(name)
        for row in datareader:
            traindata.append(row)
    return (metadata, traindata)

# Corrected usage
metadata, traindata = read_data("tennis.csv")