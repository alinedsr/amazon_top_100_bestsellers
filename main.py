#Libs
import os
import streamlit as st
import pandas as pd
import plotly.express as px

#Page Config
st.set_page_config(layout="wide")

#Title and Intro
st.title(":open_book: :rainbow[Amazon Books Reviews - 2023]", anchor=False)
st.divider()

#Dataframes
df_reviews = pd.read_csv("data/customer reviews.csv")
df_top_100_books = pd.read_csv("data/Top-100 Trending Books.csv")



#Slider
price_min: float = df_top_100_books["book price"].min()
price_max: float = df_top_100_books["book price"].max()
max_price: float = st.sidebar.slider("Price Range", price_min, price_max, price_max)
df_books = df_top_100_books[df_top_100_books["book price"] <= max_price]

#View
df_books

#Graphs
fig1 = px.bar(df_books["year of publication"].value_counts())
fig2 = px.histogram(df_books["book price"])

#Columns
col1, col2 = st.columns(2)
col1.plotly_chart(fig1)
col2.plotly_chart(fig2)