import streamlit as st
import yfinance as yf
import numpy as np

@st.cache_data
def get_metric(ticker):
    tick = yf.Ticker(ticker)
    data = tick.history(period="1wk")
    prices = data['Close']
    return {
        "ticker":ticker,
        "price":np.round(prices.values[-1],2),
        "change":str(np.round((np.diff(prices.values[-2:])/prices.values[-2]*100)[0],2))+"%"}
# get_metric("BTC")

st.title("My Portfolio")

st.sidebar.markdown("Portfolio")

tickers = ['AAPL','MSFT','BTC']
cols = st.columns(len(tickers))

for ticker,col in zip(tickers,cols):
    metric = get_metric(ticker)
    col.metric(label=metric['ticker'],value=metric['price'],delta=metric['change'])



