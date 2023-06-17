import streamlit as st
import pandas as pd
import requests
from io import BytesIO


st.write("Hello World")

st.write('# TABLE')

st.write('Below you will fin some table that will be generated as ***MAP*** and also ***CHART*** one next tab')

url = 'https://github.com/mahardisetyoso/streamlit_demo_hardy/raw/main/data/Macroeconomy%20Data%20for%20Territory_.xlsx'
xlsx = requests.get(url).content
df1 = pd.read_excel(BytesIO(xlsx),'City Level Data')

st.write('Displaying the dataframe: `df`')
st.write(df1.head())

st.write('Using the `describe` method:')
st.write(df1.describe())
