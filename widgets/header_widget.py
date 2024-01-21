import streamlit as st


def header_widget(title, isHeader):
    if isHeader:
        return st.header(title, divider='rainbow')
    else:
        return st.subheader(title, divider='blue')