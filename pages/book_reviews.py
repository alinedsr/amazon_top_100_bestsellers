import streamlit as st
import pandas as pd
from st_pages import Page, show_pages

#Page Config
st.set_page_config(page_title="Prices", layout="wide")

#Title and Intro
st.title(":open_book: :rainbow[Amazon Books Reviews - 2023]", anchor=False)
st.divider()

# Specify what pages should be shown in the sidebar, and what their titles 
# and icons should be
show_pages(
    [
        Page("main.py", "Prices", ":home:"),
        Page("pages/book_reviews.py", "Reviews", ":books:")
    ]
)

#Dataframes
df_reviews = pd.read_csv("data/customer reviews.csv")
df_top_100_books = pd.read_csv("data/Top-100 Trending Books.csv")

books = df_top_100_books["book title"].unique()
book = st.sidebar.selectbox("Books", books)

df_book = df_top_100_books[df_top_100_books["book title"] == book]

df_reviews_f = df_reviews[df_reviews["book name"] == book]

book_title = df_book["book title"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_price = f'${df_book["book price"].iloc[0]}'
book_rating = f'{df_book["rating"].iloc[0]}  %'
book_year = df_book["year of publication"].iloc[0]

st.title(book_title)
st.subheader(book_genre)
col1, col2, col3 = st.columns(3)
col1.metric("Price", book_price)
col2.metric("Rating", book_rating)
col3.metric("Year of Publication", book_year)

st.divider()

for book in df_reviews_f.values:
    message = st.chat_message(f"{book[4]}")
    message.write(f"**{book[2]}**")
    message.write(f"{book[5]}")