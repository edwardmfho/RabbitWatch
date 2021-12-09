import pandas as pd
import streamlit as st


def load_data(data_url, nrows=None):
    data = pd.read_csv(data_url, nrows=nrows)
    return data
