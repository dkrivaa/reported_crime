import streamlit as st
import time

from functions.data import startup

st.title('Reported Crime')

data = startup()

period = [f'{item[0]}_{item[1]}' for item in data]
chart_data = [len(item[2]) for item in data]

st.write(period)
st.write(chart_data)



