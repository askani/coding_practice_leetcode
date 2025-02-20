import numpy as np

# Generate sample data
np.random.seed(42)
X = np.random.rand(100)  # 100 data points
y = 3 * X + 2 + np.random.randn(100) * 0.1  # y = 3x + 2 + noise

# Hyperparameters
learning_rate = 0.1
epochs = 3000

# Initialize parameters
m = np.random.randn()
b = np.random.randn()

# Gradient Descent
for _ in range(epochs):
    y_pred = X * m + b  # Predicted values
    error = y - y_pred

    # Compute gradients
    dm = -2 * np.sum(X * error) / len(X)
    db = -2 * np.sum(error) / len(X)

    # Update parameters
    m -= learning_rate * dm
    b -= learning_rate * db

# Print final model
print(f"Final model: y = {m:.2f}x + {b:.2f}")
