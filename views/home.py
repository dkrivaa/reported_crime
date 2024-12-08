import pandas as pd
import streamlit as st
import altair as alt
from functions.data import startup

st.title('Reported Crime')

data = startup()

quarter_crime = [len(data[i]) for i in range(len(data))]
name = [f'{data[i]['Year'].unique().tolist()[0]}_{data[i]['Quarter'].unique().tolist()[0]}'
        for i in range(len(data))]
df = pd.DataFrame(quarter_crime, name)

st.bar_chart(df)

st.write(df)


