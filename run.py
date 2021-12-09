import streamlit as st
import pandas as pd

from data import load_data
from datetime import timedelta, datetime
from config import site_config, site_header_info
from metric import get_metric
# Import Site Configs
site_config()

# Text + Image for Site
site_header_info()

# Show Metric Data
get_metric()

display_choice = st.selectbox('Days ', ['Mosquitos and Insects Report',
                                                  'Unusual Death/Illness Report',
                                                  'Lost Rabbit Report'])
if display_choice == 'Mosquitos and Insects Report':
    data = load_data('dataset/insect_report.csv')
    data['report_datetime'] = pd.to_datetime(data['report_datetime'])
    st.subheader('Mosquitos and Insects Report')

    # days_to_filter = st.slider('Days', 1, 100, 14)
    #
    # st.markdown(f'**Data of the past {days_to_filter} days**')
    # filtered_data = data[data['report_datetime'] - datetime.today() <= timedelta(days=days_to_filter)]

    st.map(data)

# Filter out by state
# choices = st.multiselect('State(s)', ['NSW', 'VIC', 'TAS', 'ACT', 'NT', 'QLD', 'WA'])
elif display_choice == 'Unusual Death/Illness Report':
    data = load_data('dataset/ind_report.csv')
    st.subheader('Unusual Death/Illness Report')
    death_df = data[data['flag_death'] == 1]
    illness_df = data[data['flag_illness'] == 1]
    st.markdown('At a glance')

    st.markdown('Death Map')
    st.map(death_df)
    st.markdown('Illness Map')
    st.map(illness_df)

else:
    st.subheader('Lost Rabbit Report')
