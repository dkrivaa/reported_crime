import streamlit as st
import pandas as pd
import requests
import json



def resources():
    return {
        2019: '3b3cf0d8-67d9-4719-9dfa-f73ab7ab9f68',
        2020: '520597e3-6003-4247-9634-0ae85434b971',
        2021: '3f71fd16-25b8-4cfe-8661-e6199db3eb12',
        2022: 'a59f3e9e-a7fe-4375-97d0-76cea68382c1',
        2023: '32aacfc9-3524-4fba-a282-3af052380244',
        2024: '5fc13c50-b6f3-4712-b831-a75e0f91a17e',
    }


def quarters():
    return ['Q1', 'Q2', 'Q3', 'Q4']


def get_data(resource_id, filters=None):
    if filters is None:
        filters = {}

    url = 'https://data.gov.il/api/3/action/datastore_search'

    offset = 0
    limit = 100000  # Fetch in chunks
    all_records = []

    while True:
        # Define API request parameters
        params = {
            "resource_id": resource_id,
            "limit": limit,
            "offset": offset,
            'filters': json.dumps(filters)
        }

        response = requests.get(url, params=params)
        if response.status_code != 200:
            st.write(f"Error fetching resource {resource_id}: {response.status_code}")
            break

        data = response.json()
        if not data.get("success"):
            st.write(f"Error in response for {resource_id}: {data.get('error')}")
            break

        # Extract records
        records = data["result"]["records"]
        if not records:
            break

        all_records.extend(records)
        offset += limit

    df = pd.DataFrame(all_records)

    # return len(all_records)
    return df


@st.cache_data(show_spinner='Loading data.......', persist='disk')
def startup():
    return [(next((k for k, v in resources().items() if v == resource), None), quarter,
             pd.DataFrame(get_data(resource, filters={'Quarter': quarter, })))
            for resource in resources().values()
            for quarter in quarters()]



