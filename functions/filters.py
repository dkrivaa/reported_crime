import streamlit as st
import pandas as pd


# Filter functions
def filter_by_yeshuv(df, yeshuvKod=None):
    if yeshuvKod is not None:
        return df[df['YeshuvKod'] == yeshuvKod]
    else:
        return


def filter_by_district(df, districtKod=None):
    if districtKod is not None:
        return df[df['PoliceDistrictKod'] == districtKod]
    else:
        return


def filter_by_merhav(df, merhavKod=None):
    if merhavKod is not None:
        return df[df['PoliceMerhavKod'] == merhavKod]
    else:
        return


def filter_by_station(df, stationKod=None):
    if stationKod is not None:
        return df[df['PoliceStationKod'] == stationKod]
    else:
        return


def filter_by_crimeGroup(df, crimeGroupKod=None):
    if crimeGroupKod is not None:
        return df[df['StatisticGroupKod'] == crimeGroupKod]
    else:
        return


def filter_by_crimeType(df, crimeTypeKod=None):
    if crimeTypeKod is not None:
        return df[df['StatisticTypeKod'] == crimeTypeKod]
    else:
        return


def selection_filter(df, k, v=None):
    if v is not None:
        return df[df[k] == v]
    else:
        return df


def use_filters(df, filter_dict):
    filtered_df = df
    for k, v in filter_dict.items():
        filtered_df = selection_filter(filtered_df, k, v)
    return filtered_df.shape[0]
