import pandas as pd
import streamlit as st
import altair as alt

from functions.data import startup
from functions.form_elements import yeshuv_element, district_element, merhav_element, station_element

st.title('Reported Crime')
st.divider()

# Get data and keep in cache
data = startup()

quarter_crime = [data[i].shape[0] for i in range(len(data))]

with st.expander('Select data'):
    yeshuv = yeshuv_element()
    if yeshuv is not None:
        yeshuvKod = [k for k, v in st.session_state['yeshuv_dict'].items() if v == yeshuv][0]
        st.write()

        quarter_crime = [data[i].loc[data[i]['YeshuvKod'] == yeshuvKod].shape[0] for i in range(len(data))]

    district = district_element()
    if district is not None:
        districtKod = [k for k, v in st.session_state['district_dict'].items() if v == district][0]

        merhav = merhav_element(districtKod)
        if merhav is not None:
            merhavKod = [k for k, v in st.session_state['merhav_dict'].items() if v == merhav][0]

            station = station_element(merhavKod)
            if station is not None:
                stationKod = [k for k, v in st.session_state['station_dict'].items() if v == station][0]

        # quarter_crime = [data[i].loc[data[i]['PoliceDistrictKod'] == districtKod].shape[0] for i in range(len(data))]



name = [f'{data[i]['Year'].unique().tolist()[0]}_{data[i]['Quarter'].unique().tolist()[0]}'
        for i in range(len(data))]
df = pd.DataFrame(quarter_crime, name, columns=['Data'])

st.bar_chart(df)

if st.button('Chart Data'):
    st.write('')
    st.write(df)



