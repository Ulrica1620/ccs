import streamlit as st
from PIL import Image
import os
dir_path = os.path.split(os.path.realpath(__file__))[0]
import sys
sys.path.append(dir_path)

st.set_page_config(
    page_title="新粉指南",
    page_icon=":Shark:",
    layout='wide'
)

st.title('🦈 新粉指南')

st.subheader('In progress')