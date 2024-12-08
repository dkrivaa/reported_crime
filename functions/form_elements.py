import streamlit as st
import pandas as pd


def geography():
    return st.radio('Select', ['Municipality', 'Police Territory'], index=None)


def yeshuv_element():
    options = sorted(st.session_state['yeshuv_dict'].values())
    return st.selectbox('Municipality', options=options, index=None)


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
    if merhavKod is None:
        return st.selectbox('Police Station', options=st.session_state['station_dict'].values(), index=None)
    elif merhavKod is not None:
        stations = st.session_state['merhav_station_dict'][merhavKod]
        options = [st.session_state['station_dict'][station] for station in stations]
        return st.selectbox('Police Station', options=options, index=None)



