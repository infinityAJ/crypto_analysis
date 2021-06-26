import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

menu_items = [
    'Home',
    'Analyse Crypto by Market',
    'Analyse Crypto by Time',
    'Analyse Crypto by Close Prices',
    ]

x = 10

st.set_page_config(
    page_title = "Analysis of CryptoCurrency Dataset",
    page_icon = "bitcoin icon.png"
)

st.sidebar.header("Analysis of CryptoCurrency Dataset")
st.sidebar.image('crypto.jpeg')
menu = st.sidebar.selectbox('Navigate through pages', menu_items)
df = pd.read_csv('crypto-markets.csv')
df_max = pd.read_csv('crypto_max.csv')

if menu == 'Home':
    st.title("Welcome to Crypto Currency Analysis")
    col1, col2 = st.beta_columns([2,1])
    col1.write("Hey there,\n\nThis project is made to compare and analyze the data of Crypto Currencies.\n\nBy Anant Jain")
    col2.image("bitcoin icon.png")

    st.header("A slight look of the data")
    st.write("  ")
    st.write(df.head(x))
    st.markdown("<hr>", unsafe_allow_html= True)
    col1, col2 = st.beta_columns(2)
    col1.subheader("Number of Rows:")
    col1.write(df.shape[0])
    col2.subheader("Number of Columns:")
    col2.write(df.shape[1])
    st.markdown("<hr>", unsafe_allow_html= True)

    st.header("Crypto Currency Dataset Summary")
    st.write(" ")
    st.write(df.describe())

    st.header("Columns description")
    for i in df.columns:
        st.subheader(i)
        col1, col2 = st.beta_columns(2)
        col1.caption("Unique Values")
        col1.write(len(df[i].unique()))
        col2.caption("Type of Data")
        col2.write("String of Characters" if type(df[i].iloc[0]) is str else "Numerical")
        st.markdown("<hr>",unsafe_allow_html = True)

if menu == menu_items[1]:
    st.title(menu_items[1])
    st.header("Performance of top 10 CryptoCurrencies according to rank")
    ranked_df = df[df.date=='2018-11-29'].sort_values(by=['ranknow']).head(x)
    fig = px.bar(ranked_df, x='name', y='market')
    st.plotly_chart(fig)
    st.write("We can clearly see that Bitcoin is ranked highest and also has the much higher market value then the rest.")
    

if menu == menu_items[2]:
    st.title(menu_items[2])
    st.header("Performance of Oldest Cryptocurrency - Bitcoin")
    old = pd.read_csv('old.csv')
    temp = df[df.name == old.name.iloc[0]].tail(180)
    fig = px.line(temp, x='date', y='close')
    st.plotly_chart(fig)
    st.write('Bitcoin drastically lowered in price in fall of 2018.')
    st.markdown("<hr>", unsafe_allow_html=True)
    new = pd.read_csv('new.csv')
    new_name = new.name.iloc[9]
    st.header(f"Performance of Newest CryptoCurrency - {new_name}")
    temp = df[df.name == new_name]
    fig = px.line(temp, x='date', y='close')
    st.plotly_chart(fig)
    st.write(f"{new_name}'s price went straight down in a day.")
    

if menu == menu_items[3]:
    st.title(menu_items[3])
    st.header("Highest All time closing prices of top 10 CryptoCurrencies")
    cl_sort = df_max.sort_values(by=['close'], ascending=False).head(x)
    fig = px.bar(cl_sort, x='name', y='close')
    st.plotly_chart(fig)
    st.write("Project-X has all-time highest closing price.")

