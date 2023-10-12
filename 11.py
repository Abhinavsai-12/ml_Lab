import numpy as np
import matplotlib.pyplot as plt

# Define sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Define mean squared error loss
def mse_loss(predicted, target):
    return np.mean((predicted - target) ** 2)

# Initialize inputs, target, learning rate, and weights
x1 = 0.1
x2 = 0.4
target = 0.7
learning_rate = 0.01
w1 = np.random.rand()
w2 = np.random.rand()

print("Initial W : {:.10f} {:.10f}".format(w1, w2))  # Print initial values

# Lists to store results for plotting
predicted_output = []
network_error = []

# Training loop
for _ in range(80000):
    # Forward Pass
    y = w1 * x1 + w2 * x2
    predicted = sigmoid(y)
    err = mse_loss(predicted, target)

    predicted_output.append(predicted)
    network_error.append(err)

    # Backward Pass (Gradient Descent)
    gradient = 2 * (predicted - target) * predicted * (1 - predicted)
    grad_w1 = gradient * x1
    grad_w2 = gradient * x2

    w1 -= learning_rate * grad_w1
    w2 -= learning_rate * grad_w2

# Print final values of w1 and w2
print("Final W : {:.10f} {:.10f}".format(w1, w2))

# Plotting the results
plt.figure()
plt.plot(network_error)
plt.title("Iteration Number vs Error")
plt.xlabel("Iteration Number")
plt.ylabel("Error")
plt.show()

plt.figure()
plt.plot(predicted_output)
plt.title("Iteration Number vs Prediction")
plt.xlabel("Iteration Number")
plt.ylabel("Prediction")
plt.show()