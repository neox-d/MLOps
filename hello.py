import pandas as pd
import yfinance as yf
import streamlit as st

import datetime

st.header('Stock Market Analysis', divider='rainbow')

abbr = st.text_input("Search Stock Abbr.", "MSFT", key='placeholder')


msft = yf.Ticker(abbr)

col1, col2 = st.columns(2)

with col1:
    start = st.date_input("Enter Start Date", datetime.date(2019, 1, 1))
   
with col2:
    end = st.date_input("Enter End Date", datetime.date(2024, 1, 1))
   

hist = msft.history(period="1d", start=start, end=end)

st.dataframe(hist)

st.write('Daily Closing Price')
st.line_chart(hist['Close'])

st.write('Daily Traded Volume')
st.line_chart(hist['Volume'])

st.write("The current company is: ", abbr)