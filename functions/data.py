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

    return df


@st.cache_data(show_spinner='Loading data.......', persist='disk')
def startup():
    yeshuv_set = set()
    district_set = set()
    merhav_set = set()
    station_set = set()
    crimeGroup_set = set()
    crimeType_set = set()

    district_merhav_dict = {}
    merhav_station_dict = {}
    group_type_dict = {}

    df_list = []

    for resource in resources().values():
        for quarter in quarters():
            df = get_data(resource, filters={'Quarter': quarter, })

            if len(df) > 0:

                # Copying regional councils to municipal and multiplying code to avoid identical codes
                df['YeshuvKod'] = df['YeshuvKod'].fillna((df['municipalKod'] * 10000).where(df['municipalKod'].notna()))
                df['Yeshuv'] = df['Yeshuv'].fillna(df['municipalName'].where(df['municipalKod'].notna()))

                df = df.dropna(subset=['YeshuvKod'])

                def make_pairs(codes, names):
                    return set(zip(df[codes], df[names]))

                yeshuv_set.update(make_pairs('YeshuvKod', 'Yeshuv'))
                district_set.update(make_pairs('PoliceDistrictKod', 'PoliceDistrict'))
                merhav_set.update(make_pairs('PoliceMerhavKod', 'PoliceMerhav'))
                station_set.update(make_pairs('PoliceStationKod', 'PoliceStation'))
                crimeGroup_set.update(make_pairs('StatisticGroupKod', 'StatisticGroup'))
                crimeType_set.update(make_pairs('StatisticTypeKod', 'StatisticType'))

                def make_list_dict(varKod, targetKod, relevant_dict):
                    for varKod, targetKod in df.groupby(varKod)[targetKod]:
                        if varKod not in relevant_dict:
                            relevant_dict[varKod] = set()
                        relevant_dict[varKod].update(targetKod)

                make_list_dict('PoliceDistrictKod', 'PoliceMerhavKod', district_merhav_dict)
                make_list_dict('PoliceMerhavKod', 'PoliceStationKod', merhav_station_dict)
                make_list_dict('StatisticGroupKod', 'StatisticTypeKod', group_type_dict)

                columns_to_drop = ['FictiveIDNumber', 'Yeshuv', 'PoliceDistrict', 'PoliceMerhav',
                                   'PoliceStation', 'municipalKod', 'municipalName', 'StatisticAreaKod',
                                   'StatisticArea', 'StatisticGroup', 'StatisticType']
                df.drop(columns=columns_to_drop, inplace=True)

                df_list.append(df)

    def make_dict(name, pair_set):
        if name not in st.session_state:
            st.session_state[name] = dict(pair_set)

    make_dict('yeshuv_dict', yeshuv_set)
    make_dict('district_dict', district_set)
    make_dict('merhav_dict', merhav_set)
    make_dict('station_dict', station_set)
    make_dict('crimeGroup_dict', crimeGroup_set)
    make_dict('crimeType_dict', crimeType_set)

    def parent_dict(name, relevant_dict):
        if name not in st.session_state:
            st.session_state[name] = relevant_dict

    parent_dict('district_merhav_dict', district_merhav_dict)
    parent_dict('merhav_station_dict', merhav_station_dict)
    parent_dict('group_type_dict', group_type_dict)

    return df_list








