import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('Picture1.png'))

st.header('Nadhiar Ridho Wahyu Pradana')

st.info('Data Enthusiast with an interest in Data Science and Data Visualization')

icon_size = 20

#st_button('youtube', 'https://youtube.com/dataprofessor', 'Data Professor YouTube channel', icon_size)
#st_button('youtube', 'https://youtube.com/codingprofessor', 'Coding Professor YouTube channel', icon_size)
#st_button('medium', 'https://data-professor.medium.com/', 'Read my Blogs', icon_size)
st_button('github', 'https://github.com/nrwpradana', 'Check my Github', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/nadhiar-ridho-wahyu-pradana/', 'Follow me on LinkedIn', icon_size)
st_button('newsletter', 'mailto:nadhiar11@gmail.com', 'Mail me', icon_size)
#st_button('cup', 'https://www.buymeacoffee.com/dataprofessor/', 'Buy me a Coffee', icon_size)

st.info('Check Latest Projecr Here')

st.button('project1','https://nrwpradana-krisis-pangan-app-nqc42o.streamlitapp.com/','Tetris Capstone Project', icon_size)
