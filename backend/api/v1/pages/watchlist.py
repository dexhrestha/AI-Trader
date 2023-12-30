import streamlit as st

tabs = st.tabs(['1Y','1M','1W','1D'])

with tabs[0] as tab1Y:
    st.header('1 Year Data')


with tabs[1] as tab1Y:
    st.header('1 Month Data')


with tabs[2] as tab1Y:
    st.header('1 Week Data')


with tabs[3] as tab1Y:
    st.header('1 Day Data')

