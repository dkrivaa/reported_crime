import streamlit as st
import time

from functions.data import startup

st.title('Reported Crime')

data = startup()

period = [f'{df[i]['Year']}_{df[i]['Quarter']}' for df in data for i in range(len(df))]
# chart_data = [len(item[2]) for item in data]

st.write(period)
# st.write(chart_data)



