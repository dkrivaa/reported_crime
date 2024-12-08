import streamlit as st
import pandas as pd


def district_element():
    return st.selectbox('Police District', options=st.session_state['district_dict'].values(), index=None)


def merhav_element(districtKod=None):
    if districtKod is None:
        return st.selectbox('Police Area', options=st.session_state['merhav_dict'].values(), index=None)
    elif districtKod is not None:
        merhavim = st.session_state['district_merhav_dict'][districtKod]
        options = [st.session_state['merhav_dict'][merhav] for merhav in merhavim]
        return st.selectbox('Police Area', options=options, index=None)


def station_element(merhavKod=None):
    pass



