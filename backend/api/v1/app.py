import yfinance as yf

import streamlit as st
from st_pages import Page,show_pages,add_page_title

show_pages([
    Page('app.py',"Home"),
    Page("pages/portfolio.py","Portfolio"),
    Page("pages/watchlist.py","Watchlist"),
    Page("pages/search.py","Search"),
    Page("pages/calendar.py","Calendar"),
    Page("pages/notifications.py","Notifications"),
])


import pandas as pd
import numpy as np

st.title("Stock Price Tracker")
st.sidebar.markdown("")

@st.cache_data
def load_data(period="1mo"):
    aapl = yf.Ticker("MSFT")
    data = aapl.history(period=period)
    return data 


data_load_state = st.text("Loading data...")

data = load_data("1y")


data_load_state.text('Completed')


st.subheader("Raw data")
st.write(data)

st.subheader('Stock prices')
st.line_chart(data)

