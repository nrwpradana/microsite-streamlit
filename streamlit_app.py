import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

st.set_page_config(page_title='NRWP', page_icon = "😎")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('Picture1.png'))

st.header('Nadhiar Ridho Wahyu Pradana')

st.info('Data Enthusiast with an interest in Data Science and Data Visualization')

icon_size = 25

st_button('github', 'https://github.com/nrwpradana', ' Check my Github', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/nadhiar-ridho-wahyu-pradana/', ' Follow me on LinkedIn', icon_size)
st_button('projector', 'https://www.linkedin.com/in/nadhiar-ridho-wahyu-pradana/', ' See my Tableau Public', icon_size)