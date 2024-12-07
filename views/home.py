import streamlit as st
import time

from functions.data import startup

st.title('Reported Crime')

with st.spinner('Loading Data......'):
    startup()

for key in st.session_state.keys():
    st.write(f"- {key}: {st.session_state[key]}")

