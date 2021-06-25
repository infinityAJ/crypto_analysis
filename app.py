import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import StandardScaler

com_no = st.sidebar.selectbox("comparison or specatation?","single company,comparison in 2".split(','))

menu = st.sidebar.selectbox("navigate through pages","line chart,candlestick chart,description,bar".split(','))
data = pd.read_csv('crypto-markets.csv')

com1 = st.sidebar.selectbox("please select a company...", tuple(set(data.name)), key = 'com1')

df1 = data[data.name == com1]

if com_no.startswith('comparison'):
    com2 = st.sidebar.selectbox("please select a company...", tuple(set(data.name)), key = 'com2')
    df2 = data[data.name == com2]
    #scaler = StandardScaler()
    #scaler.fit([df1.close, df2.close])
    temp1 = pd.DataFrame({'date':df1.date, com1:df1.close})
    temp2 = pd.DataFrame({'date':df2.date, com2:df2.close})
    #frame = {'date':df1.date, 'close1':df1.close,'close2':df2.close}
    df3 = pd.merge(temp1, temp2, on='date', how='inner')

if menu.startswith('line'):
    if com_no.startswith('com'):
        fig = px.line(df3, x='date', y=df3.columns[1:])
    else:
        fig = px.line(df1, x='date', y='close')
    st.plotly_chart(fig)

if menu.startswith('candle'):
    st.title(f"Candle Stick Plot of {com1}")
    fig = go.Figure(data=[go.Candlestick(x=df1['date'],open=df1['open'],
            high=df1['high'],low=df1['low'],close=df1['close'])])
    st.plotly_chart(fig)
    try:
        st.title(f"Candle Stick Plot of {com2}")
        fig2 = go.Figure(data=[go.Candlestick(x=df2['date'],open=df2['open'],
                    high=df2['high'],low=df2['low'],close=df2['close'])])
        st.plotly_chart(fig2)
    except:
        pass

if menu.startswith('des'):
    st.title(f"Describing the data of {com1}")
    des = pd.DataFrame(df1.describe())
    st.write(des)
    try:
        st.title(f"Describing the data of {com2}")
        des2 = pd.DataFrame(df2.describe())
        st.write(des2)
    except:
        pass

if menu.startswith('bar'):
    st.title(f"Bar chart of {com1}")
    fig = px.bar(df1,x='date', y='close')
    st.plotly_chart(fig)
    try:
        st.title(f"Bar chart of {com2}")
        fig2 = px.bar(df2,x='date', y='close')
        st.plotly_chart(fig2)
    except:
        pass
