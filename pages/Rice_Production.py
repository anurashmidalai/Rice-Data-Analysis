import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "assets")
IMAGE1_PATH = os.path.join(dir_of_interest, "images", "logo.jpg")

im = image.imread(IMAGE1_PATH)
st.set_page_config("Anurashmi Dalai", page_icon= im)

st.markdown(hide_default_format, unsafe_allow_html=True)
# absolute path to this file

st.title("Dashboard - Rice Data")
IMAGE_PATH = os.path.join(dir_of_interest, "images", "rice.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "rice.csv")
img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
df = df[(df["Year"]<2020)]

st.dataframe(df)

area = st.selectbox("Select the Country:", df['Area'].unique())

col1, col2 = st.columns(2, gap="large")

fig_1 = px.histogram(df[df['Area'] == area], y= "Value", x="Year", title = "Histogram")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.bar(df[df['Area'] == area], y= "Value", x="Year", title="Bar Graph")
col2.plotly_chart(fig_2, use_container_width=True)

fig_3 = px.line(df, y = "Value", x = "Year", color = "Area", title = "Line Plot Of All Available Data")
fig_4 = px.bar(df, y= "Value", x="Year", title="Bar Graph Of All Available Data", color = "Area",)

st.plotly_chart(fig_3, use_container_width=True)
st.plotly_chart(fig_4, use_container_width=True)