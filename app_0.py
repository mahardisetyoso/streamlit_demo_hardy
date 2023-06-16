import streamlit as st
import pandas as pd


st.write("Hello World")

st.write('# TABLE')

st.write('Below you will fin some table that will be generated as ***MAP*** and also ***CHART*** one next tab')

xls = pd.ExcelFile(r"C:\Users\Mahardi\OneDrive\Documents\python_project\Streamlit Simple Dashboard\data\Macroeconomy Data for Territory_.xlsx")

df1 = pd.read_excel(xls,'City Level Data')

st.write('Displaying the dataframe: `df`')
st.write(df1.head())

st.write('Using the `describe` method:')
st.write(df1.describe())