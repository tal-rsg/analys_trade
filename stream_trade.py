# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 11:54:56 2021

@author: ztche
"""
import streamlit as st
from datetime import datetime
import matplotlib.pyplot as plt
import yfinance as yf
from ta import add_all_ta_features
import pandas_ta
import btalib
import numpy as np
import seaborn as sns
import hvplot.pandas
import pandas as pd
import plotly.express as px

# headings
title = "options-2-trees"
st.write("by TrSg")
st.sidebar.title("Mensagem")

# user inputs on sidebar
st.sidebar.markdown("Análise de algumas ações da Ibovespa")


# back to main body
st.header("Cotacação Bitcoin")
st.markdown("Dados extraidos Yahoo! Finance's API biblioteca yfinance [https://pypi.org/project/yfinance/].")

#st.subheader('Key:')
#st.markdown("✅ Stock tree: black")
#call = st.checkbox('Call tree: blue')
#put = st.checkbox('Put tree: red')

# data BTC
data_btc = yf.download('BTC-USD', start = '2020-01-01')
df_btc = pd.DataFrame(data_btc)

# plot exercise price reference
# Assuming 'Close' is the column you want to plot
df_btc['Close'].plot(figsize=(12, 6))
plt.title('BTC-USD Close Price')
plt.ylabel('Price')
plt.xlabel('Date')
st.pyplot(plt)

# text section
st.header("Cotação Itaú")

# data Itau
df_acao_ita = yf.download('ITUB4.SA', start = '2020-01-01')

# Assuming 'Close' is the column you want to plot
df_acao_ita['Close'].plot(figsize=(12, 6))
plt.title('ITUB4.SA Close Price')
plt.ylabel('Price')
plt.xlabel('Date')
st.pyplot(plt)

st.header("Cotação BBA")

# data bba
df_acao_bba = yf.download('BBAS3.SA', start = '2020-01-01')

# Create a plotly figure
df_acao_bba_st = df_acao_bba.stack()
df_acao_bba_st2 = df_acao_bba_st.reset_index()
fig = px.line(df_acao_bba_st2, x='Date', y='Close', title='BBAS3.SA Close Price')  # Use 'index' if Date is the index
fig.update_layout(xaxis_title='Date', yaxis_title='Price')  # Update layout

st.plotly_chart(fig)