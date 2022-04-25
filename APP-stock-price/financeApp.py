from mimetypes import init
import yfinance as yf
import pandas as pd
import streamlit as st

st.write(""" 
Rodrigo's stock price app
prueba de app usando streamlit
 """)

nameTicker = st.text_input("Enter stock ticker", "Type Here ...") 
#initialDate = st.text_input("Enter inital date", "Type Here yyyy-m-dd") 
#finalDate = st.text_input("Enter final date", "Type Here yyyy-m-dd") 

if (st.button('Submit')): 
    result = nameTicker.title() 
    st.success(result)

tickerData = yf.Ticker(nameTicker)

tickerDF = tickerData.history(period='1d', start='2022-01-01', end='2022-04-22')

st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)

