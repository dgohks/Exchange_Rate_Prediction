# Exchange_Rate_Prediction
This project uses the ARIMA (AutoRegressive Integrated Moving Average) model to predict future exchange rates based on historical data. Done on Python 3.11.5.

## Requirements

- Python 3.11.x or above
- pandas
- matplotlib
- scikit-learn
- statsmodels

You can install the required packages using pip:

```bash
pip install pandas matplotlib scikit-learn statsmodels
```

## Usage

1. Load your data into a CSV file. The file should have two columns: "day after 1/Nov/2023" (representing the days) and "myr_usd" (representing the exchange rate).

2. Run the script `pred.py`:

```bash
python pred.py
```

The script will load the data, check for null values, plot the original data, split the data into training and testing sets, train the ARIMA model, evaluate the model using the mean squared error, and print the test MSE.

## Customization

You can customize the ARIMA model parameters (p, d, q) in the `ARIMA(train_data, order=(5,1,0))` line. You might need to adjust these parameters to get the best prediction accuracy for your data.

## Output

The script will output a plot of the original data and the mean squared error of the model. The mean squared error is a measure of the model's prediction accuracy: the lower the MSE, the better the model's predictions.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
