import pandas as pd
import streamlit as st
import altair as alt

from functions.data import startup
from functions.form_elements import district_element

st.title('Reported Crime')
st.divider()

# Get data and keep in cache
data = startup()

with st.expander('Select data'):
    district = district_element()
    if district is not None:
        districtKod = [k for k, v in st.session_state['district_dict'].items() if v == district][0]
        st.write(districtKod)

        quarter_crime = [data[i].loc[data[i]['PoliceDistrictKod'] == districtKod].shape[0] for i in range(len(data))]
        st.write(quarter_crime)
        name = [f'{data[i]['Year'].unique().tolist()[0]}_{data[i]['Quarter'].unique().tolist()[0]}'
                for i in range(len(data))]
        df = pd.DataFrame(quarter_crime, name, columns=['Data'])

        st.bar_chart(df)

        if st.button('Chart Data'):
            st.write('')
            st.write(df)

    st.write(st.session_state['district_merhav_dict'])


