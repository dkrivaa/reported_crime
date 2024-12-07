import streamlit as st

from functions.data import startup

st.title('Reported Crime')

with st.spinner('Loading Data......'):
    startup()

st.write(st.session_state)

