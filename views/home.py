import streamlit as st
import time

from functions.data import startup

st.title('Reported Crime')

data = startup()

st.write(len(data))

for i in range(len(data)):
    st.write(len(data[i]))


