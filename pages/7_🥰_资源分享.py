import streamlit as st
from PIL import Image
import os
dir_path = os.path.split(os.path.realpath(__file__))[0]
import sys
sys.path.append(dir_path)

st.set_page_config(
    page_title="资源分享",
    page_icon=":Love:",
    layout='wide'
)
# Add custom CSS to hide the GitHub icon
st.markdown("""
        <style>
        [data-testid="stToolbarActions"] {display: none}
        <style>
        """,unsafe_allow_html=True)

st.title('🥰 资源分享')

st.subheader('In progress')