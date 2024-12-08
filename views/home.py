import streamlit as st
import time

from functions.data import startup

st.title('Reported Crime')

data = startup()

quarter_crime = [len(data[i]) for i in range(len(data))]
st.write(quarter_crime)


