import streamlit as st
import time

from functions.data import startup

st.title('Reported Crime')

data = startup()

st.write(len(data))

st.write(st.session_state['district_dict'])



