import streamlit as st
from datetime import date
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

# Define global variables
START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title('Stock Forecast App')

stocks = ('GOOG', 'AAPL', 'MSFT', 'HDB','SBI','TCS','NTPC.BO')
selected_stock = st.selectbox('Select dataset for prediction', stocks)

n_years = st.slider('Years of prediction:', 1, 4)
period = n_years * 365

# Cache the data loading function to improve performance
@st.cache_data
def load_data(ticker):
    try:
        data = yf.download(ticker, START, TODAY)
        data.reset_index(inplace=True)
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

data_load_state = st.text('Loading data...')
data = load_data(selected_stock)

if data is not None:
    data_load_state.text('Loading data... done!')
    st.subheader('Raw data')
    st.write(data.tail())

    # Plot raw data
    def plot_raw_data(data):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open", line=dict(color='orange')))
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
        fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)

    plot_raw_data(data)

    # Prepare data for Prophet model
    df_train = data[['Date', 'Close']]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

    # Fit the model
    m = Prophet()
    m.fit(df_train)

    # Create future dataframe and predict
    future = m.make_future_dataframe(periods=period)
    forecast = m.predict(future)

    # Display forecast data
    st.subheader('Forecast data')
    st.write(forecast.tail())

    # Plot the forecast with an orange line
    forecast_fig = plot_plotly(m, forecast)
    for trace in forecast_fig['data']:
        trace['line']['color'] = 'orange'
    st.plotly_chart(forecast_fig)

    st.write("Forecast components")
    components_fig = m.plot_components(forecast)
    st.write(components_fig)
else:
    st.error("No data loaded")
