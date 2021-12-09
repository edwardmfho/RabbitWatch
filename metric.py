import streamlit as st
import pandas as pd
from datetime import datetime
from data import load_data


def load_metric_data(metric_type):
    if metric_type == 'insect':
        df = load_data('dataset/insect_report.csv')
        addition = df.groupby('report_datetime').count()
        metric = (len(df), addition['suburb_name'].iloc[-1])
        return metric
    else:
        metric = (10, 1)
        return metric

def get_metric():
    insects_report = load_metric_data('insect')
    now = datetime.now()
    st.markdown(f'**As of {now.strftime("%m/%d/%Y")}: **')
    col1, col2, col3 = st.columns(3)

    col1.metric('Insects Report', load_metric_data('insect')[0], load_metric_data('insect')[1].astype(str))
    col2.metric('Illness Report', load_metric_data('illness')[0], load_metric_data('illness')[1])
    col3.metric('Death Report', load_metric_data('death')[0], load_metric_data('death')[1])
    st.caption('Recording since 2021/12/31')