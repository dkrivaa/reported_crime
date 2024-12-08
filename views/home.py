import pandas as pd
import streamlit as st
import altair as alt
from functions.data import startup

st.title('Reported Crime')

data = startup()

quarter_crime = [len(data[i]) for i in range(len(data))]
name = [f'{data[i]['Year'].unique().tolist()[0]}_{data[i]['Quarter'].unique().tolist()[0]}'
        for i in range(len(data))]
df = pd.DataFrame(quarter_crime, name)

# st.bar_chart(df)

chart = alt.Chart(df).mark_bar().encode(
    x='name',
    y=alt.Y('quarter_crime', scale=alt.Scale(domain=[75000, 105000]))
)
# Display the chart in Streamlit
st.altair_chart(chart)
st.write(df)


