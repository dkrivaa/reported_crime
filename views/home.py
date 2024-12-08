import pandas as pd
import streamlit as st
import altair as alt
from functions.data import startup

# Get data and keep in cache
data = startup()

st.title('Reported Crime')
st.divider()

with st.expander('Select data'):
    district = st.selectbox('District', options=st.session_state['district_dict'].values(), index=None)
    if district is not None:
        districtKod = (k for k, v in st.session_state['district_dict'].items() if v == district)
        st.write(districtKod)

        quarter_crime = [data[i].shape[0] for i in range(len(data))]
        st.write(quarter_crime)
        st.write(data[1])
        name = [f'{data[i]['Year'].unique().tolist()[0]}_{data[i]['Quarter'].unique().tolist()[0]}'
                for i in range(len(data))]
        df = pd.DataFrame(quarter_crime, name, columns=['Data'])

        st.bar_chart(df)

        if st.button('Chart Data'):
              st.write('')
              st.write(df)


