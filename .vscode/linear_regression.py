from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression

# Generate synthetic data
X, y = make_regression(n_samples=100, n_features=1, noise=0.1)

# Train a linear regression model
model = LinearRegression()
model.fit(X, y)

# Make a prediction
prediction = model.predict([[2.5]])
print(f"Prediction for 2.5: {prediction[0]:.2f}")