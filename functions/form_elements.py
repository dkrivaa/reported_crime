import streamlit as st
import pandas as pd

def district_element():
    return st.selectbox('Police District', options=st.session_state['district_dict'].values(), index=None)


def merhav_element(district=None):

    if district is None:
        return st.selectbox('Police Area', options=st.session_state['merhav_dict'].values(), index=None)
    elif district is not None:
        merhavim = st.session_state['district_merhav_dict'][district]
        options = [st.session_state['merhav_dict'][merhav] for merhav in merhavim]
        return st.selectbox('Police Area', options=options, index=None)




