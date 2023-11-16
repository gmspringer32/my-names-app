import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Names")

url = 'https://github.com/esnt/Data/raw/main/Names/popular_names.csv'

df = pd.read_csv(url)

selected_name = st.text_input('Enter a name', 'John')

name_df = df[df['name'] == selected_name]
if name_df.empty:
    st.write('Name not found')
else:
    fig = px.line(name_df, x = 'year', y = 'n', color = 'sex', color_discrete_sequence=px.colors.qualitative.Set2)
    st.plotly_chart(fig)

selected_year = st.selectbox('Select a year', df['year'].unique())

year_df = df[df['year'] == selected_year]
girl_names = year_df[year_df['sex'] == "F"].sort_values(by='n', ascending = False).head(5)
boy_names = year_df[year_df['sex'] == "M"].sort_values(by='n', ascending = False).head(5)

fig, ax = plt.subplots()
sns.barplot(girl_names, x = 'n', y = 'name')
st.pyplot(fig)