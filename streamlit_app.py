import streamlit
streamlit.title("My Parents New Healthy Diner")
streamlit.header("🥣 Breakfast Menu")
streamlit.text("🥗 Bread Omlette")
streamlit.text("🐔 Idli & Chutney")
streamlit.text("🥑🍞 Ravva Onion Dosa")
streamlit.text("🥑🍞 Bread Omlette")
   
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.datafrome(my_fruit_list)
