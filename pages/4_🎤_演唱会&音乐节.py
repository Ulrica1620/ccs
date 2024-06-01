import streamlit as st
from PIL import Image
import os
dir_path = os.path.split(os.path.realpath(__file__))[0]
import sys
sys.path.append(dir_path)

st.set_page_config(
    page_title="演唱会&音乐节",
    page_icon=":Mic:",
    layout='wide'
)
# Add custom CSS to hide the GitHub icon
st.markdown("""
        <style>
        [data-testid="stToolbarActions"] {display: none}
        <style>
        """,unsafe_allow_html=True)

st.title('🎤 演唱会&音乐节')

st.subheader('In progress')