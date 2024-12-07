import streamlit as st

from functions.data import resources, quarters, get_data

st.title('Reported Crime')

# data = []
# for quarter in quarters():
#     for resource in resources().values():
#         data.append(get_data(resource, filters={'Quarter': quarter}))
data = [(next((k for k, v in resources().items() if v == resource), None), quarter,
         get_data(resource, filters={'Quarter': quarter}))
        for resource in resources().values()
        for quarter in quarters()]

st.write(data)

