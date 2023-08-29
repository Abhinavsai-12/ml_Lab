import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets

def distance(instance1, instance2):
    """ Calculates the Euclidean distance between two instances"""
    return np.linalg.norm(np.subtract(instance1, instance2))

def get_neighbors(training_set, labels, test_instance, k, distance_fn):
    """
    get_neighbors calculates a list of the k nearest neighbors of an instance 'test_instance'.
    The function returns a list of k 3-tuples. Each 3-tuple consists of (index, dist, label)
    """
    distances = []
    for index in range(len(training_set)):
        dist = distance_fn(test_instance, training_set[index])
        distances.append((index, dist, labels[index]))
    distances.sort(key=lambda x: x[1])
    neighbors = distances[:k]
    return neighbors

# Load the Iris dataset
iris = datasets.load_iris()
data = iris.data
labels = iris.target

np.random.seed(42)
indices = np.random.permutation(len(data))
n_training_samples = 12
learn_data = data[indices[:-n_training_samples]]
learn_labels = labels[indices[:-n_training_samples]]

test_data = data[indices[-n_training_samples:]]
test_labels = labels[indices[-n_training_samples:]]

for i in range(5):
    neighbors = get_neighbors(learn_data, learn_labels, test_data[i], 3, distance_fn=distance)
    print("Index:", i, '\n',
          "Testset Data:", test_data[i], '\n',
          "Testset Label:", test_labels[i], '\n',
          "Neighbors:", neighbors, '\n')

# Visualize the data of the learn set
colours = ("r", "g", "y")
X = []
for iclass in range(3):
    X.append([[], [], []])
    for i in range(len(learn_data)):
        if learn_labels[i] == iclass:
            X[iclass][0].append(learn_data[i][0])
            X[iclass][1].append(learn_data[i][1])
            X[iclass][2].append(sum(learn_data[i][2:]))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for iclass in range(3):
    ax.scatter(X[iclass][0], X[iclass][1], X[iclass][2], c=colours[iclass])
plt.show()
