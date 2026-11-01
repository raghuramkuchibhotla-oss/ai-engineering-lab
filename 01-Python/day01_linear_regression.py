import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create sample data
np.random.seed(42)

hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
scores = 5 + 8 * hours + np.random.randn(10) * 4

# Step 2: Initialize parameters
weight = 0.0
bias = 0.0
learning_rate = 0.001
epochs = 5000

n = len(hours)

# Step 3: Train the model
for epoch in range(epochs):

    predictions = weight * hours + bias
    errors = predictions - scores

    loss = np.mean(errors ** 2)

    dw = (2 / n) * np.sum(errors * hours)
    db = (2 / n) * np.sum(errors)

    weight -= learning_rate * dw
    bias -= learning_rate * db

    if epoch % 500 == 0:
        print(f"Epoch {epoch}: Loss = {loss:.2f}")

# Step 4: Display results
print("\nTraining completed!")
print(f"Weight: {weight:.2f}")
print(f"Bias: {bias:.2f}")

# Step 5: Make a prediction
study_hours = 7.5
predicted_score = weight * study_hours + bias

print(f"Predicted score: {predicted_score:.2f}")

# Step 6: Visualize results
plt.scatter(hours, scores, label="Actual scores")

plt.plot(
    hours,
    weight * hours + bias,
    color="red",
    label="Predicted line"
)

plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")
plt.title("Linear Regression")
plt.legend()
plt.grid()
plt.show()