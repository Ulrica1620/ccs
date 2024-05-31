import streamlit as st
from PIL import Image
import os
dir_path = os.path.split(os.path.realpath(__file__))[0]
import sys
sys.path.append(dir_path)

st.set_page_config(
    page_title="个人奖项",
    page_icon=":trophy:",
    layout='wide'
)

st.title('🏆 个人奖项')

st.subheader('In progress')