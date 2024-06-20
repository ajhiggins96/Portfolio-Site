# Filename note: '_.py' will not show up in the sidebar.
# This functionality is used here to have a space to deploy unpolished work
# and keep it off the official portfolio.

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from utils import sidebar


st.set_page_config(page_title="Purple Martins", page_icon='🪶')

sidebar()

st.markdown("# Patty Mag's Purple Martin Plots")

def load_csv(file):
    return pd.read_csv(file, index_col=0, parse_dates=True).fillna(0).astype(int)

def plot_line(ax, data, y_label, color='purple'):
    ax.plot(data, color)
    ax.set_ylabel(y_label.title())
    plot_labeled_points(ax, data, label=y_label)

def plot_labeled_points(ax, data, label):
    dates = data.index
    for date in dates:
        y = data.loc[date]
        if y==0: 
            continue
        # TODO: emojis as markers
        # emoji = {
        #     'Nests': '🪹',
        #     'Eggs': '🥚',
        #     'Young': '🐣'
        # }
        # ax.text(date, y, s=emoji[label], ha='center', va='center')
        text = f"{y}"
        ax.text(date, y, s=text, ha='center', va='center', backgroundcolor='w')
    ax.set_xticks(dates, labels=dates.strftime('%B %d'), rotation=45, ha='right')

def load_pm_data():
    data = {}
    data['2024'] = {}
    data['2024']['eggs'] = load_csv('static/purple_martins/2024_eggs.csv')
    data['2024']['young'] = load_csv('static/purple_martins/2024_young.csv')
    data['2024']['nests'] = load_csv('static/purple_martins/2024_nests.csv')
    data['2023'] = {}
    data['2023']['eggs'] = load_csv('static/purple_martins/2023_eggs.csv')
    data['2023']['young'] = load_csv('static/purple_martins/2023_young.csv')
    data['2023']['nests'] = load_csv('static/purple_martins/2023_nests.csv')
    return data

data = load_pm_data()

with st.container(border=True):

    year = st.radio(
        label='Select year:', 
        options=['2023', '2024'], 
        index=1
    )

    fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True)
    fig.suptitle(f'{year} Purple Martin Nest Checks')
    plot_line(ax[0], data[year]['eggs'].sum(axis=1), y_label='Eggs')
    plot_line(ax[1], data[year]['young'].sum(axis=1), y_label='Young')
    st.pyplot(fig)