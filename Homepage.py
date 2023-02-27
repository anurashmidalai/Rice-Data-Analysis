import streamlit as st
from matplotlib import image
import os
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
dir_of_interest = os.path.join(FILE_DIR, "assets")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "logo.jpg")
im = image.imread(IMAGE_PATH)
st.set_page_config("Anurashmi Dalai", page_icon= im)
st.markdown(hide_default_format, unsafe_allow_html=True)
st.title("Anurashmi Dalai's Homepage")

btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("Hi! Glad you could make it to my first web application. :smile: ")
    st.balloons()