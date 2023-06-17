import streamlit as st
import pandas as pd
import geopandas as gpd
import seaborn as sns
import pydeck as pdk
import requests
from io import BytesIO
from math import floor
sns.set_theme(style="whitegrid")

url = 'https://github.com/mahardisetyoso/streamlit_demo_hardy/raw/main/data/Macroeconomy%20Data%20for%20Territory_.xlsx'
xlsx = requests.get(url).content
df1 = pd.read_excel(BytesIO(xlsx),'City Level Data')
df1_compile = df1[['Provinsi','Kab/Kota','Kec','Desa','Kel','Population','Regional GDP (IDR Bil)']]

df2_1 = pd.crosstab(index=df1_compile['Provinsi'],
           columns='GDP Province in Billion',
           values=df1_compile['Regional GDP (IDR Bil)'],
           aggfunc='sum').sort_values(by='GDP Province in Billion',ascending=False).reset_index()

df2_2 = pd.crosstab(index=df1_compile['Provinsi'],
           columns='Population',
           values=df1_compile['Population'],
           aggfunc='sum').sort_values(by='Population',ascending=False).reset_index()

df3 = pd.merge(df2_1,df2_2, on="Provinsi", how="left").sort_values(by='GDP Province in Billion',ascending=False)

file = 'https://raw.githubusercontent.com/mahardisetyoso/streamlit_demo_hardy/main/data/indonesia.geojson'

gdf = gpd.read_file(file)
gdf['Provinsi']=gdf['state'].str.upper()
gdf['Provinsi'] = gdf['Provinsi'].replace(['YOGYAKARTA','BANGKA-BELITUNG','JAKARTA RAYA'],['DAERAH ISTIMEWA YOGYAKARTA','KEPULAUAN BANGKA BELITUNG','DKI JAKARTA'])

gdf2 = pd.merge(gdf,df3, on="Provinsi", how="left")
gdf3 = gdf2.to_json()

min_count = gdf2['GDP Province in Billion'].min()
max_count = gdf2['GDP Province in Billion'].max()
diff = max_count - min_count

color_scheme = [
        [255,255,178],
        [254,217,118],
        [254, 178, 76],
        [253, 141, 60],
        [240,59,32],
        [189,0,38]
    ]

def get_color(row):
    number_of_colors = len(color_scheme)
    index = floor(number_of_colors * (row['GDP Province in Billion'] - min_count) / diff)
    # the index might barely go out of bounds, so correct for that:
    if index == number_of_colors:
        index = number_of_colors - 1
    elif index == -1:
        index = 0
    return color_scheme[index]

gdf2['color_column'] = gdf2.apply(get_color, axis=1)




layers = [
    pdk.Layer(
        type="GeoJsonLayer",
        data=gdf2,
        width_scale=20,
        width_min_pixels=5,
        get_width=5,
        get_fill_color="color_column",
        pickable=True,
        ),
]

view_state = pdk.ViewState(
    longitude=113.23833543060013,
    latitude=-4.789453431710103,
    zoom=4,
    min_zoom=2,
    max_zoom=20,
    pitch=30,
    bearing=4)


r = pdk.Deck(layers=[layers],
             initial_view_state=view_state,
             tooltip={
                'html': '<b>GDP Province</b> {Provinsi} <b>in Billion:</b> {GDP Province in Billion} <b>with Population</b> {Population}',
                
                'style': {
                    "backgroundColor": "steelblue",
                    'color': 'white'
                    }
                }
            )
st.write(' ##  MAP 🗺️')
st.pydeck_chart(r)
