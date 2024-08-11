
                                      Stock Forecast App

This application is a simple and interactive stock price forecasting tool built using Streamlit, Prophet, and yFinance.
It allows users to select a stock from a predefined list, visualize historical data, and predict future stock prices 
for up to 4 years.

Features:
- Stock Selection: Choose from a list of stocks to forecast (e.g., Google, Apple, Microsoft).
- Historical Data Visualization: Display and interact with historical stock data using Plotly.
- Stock Price Prediction: Predict future stock prices for 1 to 4 years using the Prophet model.
- Interactive Plots: Visualize the forecast and its components with customizable plots.

Requirements:
To run this application, you need to have the following Python packages installed:
- `streamlit`
- `yfinance`
- `prophet`
- `plotly`

You can install these packages using pip: pip install streamlit yfinance prophet plotly

 How to Run the App

1. Clone this repository or copy the code into a Python file (e.g., `app.py`).
2. Ensure you have all the required packages installed.
3. Run the application using Streamlit:  streamlit run yourfilename.py
4. Open the provided URL in your web browser to interact with the app.

Explanation of the Code
-Imports: The app imports necessary libraries such as `streamlit` for the web interface, `yfinance` 
                  for fetching stock data, `prophet` for forecasting, and `plotly` for interactive plots.

-Global Variables:
  - `START`: The start date for historical data retrieval.
  - `TODAY`: The current date, used as the end date for data retrieval.
  - `stocks`: A tuple containing the stock symbols available for prediction.

-User Interface:
  - The app's title is set using `st.title`.
  - Users can select a stock from a dropdown list using `st.selectbox`.
  - A slider allows users to choose the number of years for which they want to predict stock prices.

-Data Loading:
  - The 'load_data' function fetches stock data using yFinance and caches the result to improve performance.
  - The app provides feedback on the data loading status using `st.text`.

-Data Visualization:
  - A plot of the raw stock data is generated using Plotly, showing the opening and closing prices over time.

-Forecasting:
  - The historical closing prices are prepared and fed into the Prophet model.
  - The model generates predictions for the selected period.
  - The forecast is visualized, with the forecast line colored orange.

-Forecast Components:
  - The app displays the forecast components, such as trends and seasonal patterns, using Prophet's built-in plotting functions.

Troubleshooting

-Error Loading Data:If there's an issue with fetching the stock data, the app displays an error message. Ensure that you have a stable internet connection and that the stock symbol is correct.
-Prophet Installation:Installing Prophet can sometimes be tricky due to dependencies. Make sure you follow the official installation instructions or refer to the documentation for your environment.



