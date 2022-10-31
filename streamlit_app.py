import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('Picture1.png'))

st.header('Nadhiar Ridho Wahyu Pradana')

st.info('Data Enthusiast with an interest in Data Science and Data Visualization')

icon_size = 25

st_button('github', 'https://github.com/nrwpradana', ' Check my Github', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/nadhiar-ridho-wahyu-pradana/', ' Follow me on LinkedIn', icon_size)
st_button('newsletter', 'mailto:nadhiar11@gmail.com', ' Mail me', icon_size)
st_button('projector', 'https://public.tableau.com/app/profile/nadhiar', ' See my Tableau public', icon_size)

st.info('Check My Latest Project Here')

st_button('coffee','https://nrwpradana-krisis-pangan-app-nqc42o.streamlitapp.com/',' Tetris Capstone Project', icon_size)
st_button('projector','https://public.tableau.com/app/profile/nadhiar/viz/PenilaianIntegritasProvinsiJawaBarat/PenilaianIntegritasJabar',' Jabar Dataviz Fest 2022', icon_size)
