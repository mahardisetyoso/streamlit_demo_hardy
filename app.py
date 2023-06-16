import streamlit as st

from st_pages import Page, Section, add_page_title, show_pages

add_page_title(layout="wide")


st.write("# Welcome to Streamlit! 👋")

show_pages(
     [
        Page("app_0.py","Home","🏠"),
        Page("app_1.py","Map","🗺️"),
        Page("app_2.py","Charts","📊")
    ]
 )
