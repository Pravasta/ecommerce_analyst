import streamlit as st

def slider_widgets(min_date, max_date):

    slider = st.sidebar.image("assets/logo.png")

    start_date, end_date = st.sidebar.date_input(
        label='Rentang Waktu', min_value=min_date,
        max_value=max_date,
        value=[min_date,max_date]
    )


    return [slider, start_date, end_date]