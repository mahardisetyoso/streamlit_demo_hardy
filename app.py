import streamlit as st
from st_pages import Page, show_pages, add_page_title

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")

show_pages(
    [
        Page("app_0.py","Home","🏠"),
        Page("app_1.py","Map","🗺️"),
        Page("app_2.py","Charts","📊")
    ]
)
