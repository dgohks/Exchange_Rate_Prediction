import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error

# Load the data
data = pd.read_csv('exchangerates.csv')

# Check for null values
print(data.isnull().sum())

# Plot the data
plt.plot(data["day after 1/Nov/2023"], data['myr_usd'], color='blue')

# Split the data
train_data, test_data = train_test_split(data['myr_usd'], test_size=0.2, shuffle=False)

# Train the model
model = ARIMA(train_data, order=(5,1,0))
model_fit = model.fit()

# Evaluate the model
predictions = model_fit.predict(start=len(train_data), end=len(train_data) + len(test_data)-1, dynamic=False)
error = mean_squared_error(test_data, predictions)
print('Test MSE: %.3f' % error)

# Predict the future movement
future_days = pd.RangeIndex(start=data['day after 1/Nov/2023'].max(), stop=data['day after 1/Nov/2023'].max() + 2)
future_movement = model_fit.predict(start=len(data), end=len(data) + 1)
plt.plot(future_days, future_movement, color='red')
plt.show()

print(future_movement)