import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests
from io import BytesIO
from math import floor
sns.set_theme(style="darkgrid")

url = 'https://github.com/mahardisetyoso/streamlit_demo_hardy/raw/main/data/Macroeconomy%20Data%20for%20Territory_.xlsx'
xlsx = requests.get(url).content
df1 = pd.read_excel(BytesIO(xlsx),'City Level Data')
df1_compile = df1[['Provinsi','Kab/Kota','Kec','Desa','Kel','Population','Regional GDP (IDR Bil)']]

df1_compile.sort_values(by='Regional GDP (IDR Bil)',ascending=False)

df2_1 = pd.crosstab(index=df1_compile['Provinsi'],
           columns='GDP Province in Billion',
           values=df1_compile['Regional GDP (IDR Bil)'],
           aggfunc='sum').sort_values(by='GDP Province in Billion',ascending=False).reset_index()

df2_2 = pd.crosstab(index=df1_compile['Provinsi'],
           columns='Population',
           values=df1_compile['Population'],
           aggfunc='sum').sort_values(by='Population',ascending=False).reset_index()

df3 = pd.merge(df2_1,df2_2, on="Provinsi", how="left").sort_values(by='GDP Province in Billion',ascending=False)
df4 = df3[:10]

sns.set_color_codes("muted")
fig, ax = plt.subplots()
ax = sns.barplot(x="GDP Province in Billion", y="Provinsi", data=df4,
            label="GDP Province in Billion", color="r")

st.write('## Charts 📊')
st.pyplot(fig)
