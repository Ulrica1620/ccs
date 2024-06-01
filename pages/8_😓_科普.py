import streamlit as st
from PIL import Image
import os
dir_path = os.path.split(os.path.realpath(__file__))[0]
import sys
sys.path.append(dir_path)

st.set_page_config(
    page_title="科普",
    page_icon=":Scroll:",
    layout='wide'
)

# Add custom CSS to hide the GitHub icon
st.markdown("""
        <style>
        [data-testid="stToolbarActions"] {display: none}
        <style>
        """,unsafe_allow_html=True)

st.title('😓 科普')

st.subheader('In progress')