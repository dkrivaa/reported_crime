import streamlit as st
import time

from functions.data import startup

st.title('Reported Crime')

with st.spinner('Loading Data......'):
    data = startup()

st.write(data)



