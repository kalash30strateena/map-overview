import streamlit as st
st.set_page_config(layout="wide")
from components.styles import apply_global_styles # type: ignore
from components.logged_header import logged_header
logged_header()
apply_global_styles()

import streamlit.components.v1 as components

with open("new_map.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=600, width=1200, scrolling=False)
