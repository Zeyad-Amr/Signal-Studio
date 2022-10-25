import streamlit as st
from ui.views.header import headerui
from ui.views.signalsPanel import signalsPanel
from ui.views.operationsPanel import operationsPanel
from ui.views.signalGraph import signalGraph
from stateManagement.stateManagement import stateManagement


class Appui:
    def __init__(self):

        # stateManagement
        state = stateManagement()
        # config
        st.set_page_config(page_title='Sampling Studio')

        # styling injection
        with open("./styles/style.css") as source:
            style = source.read()
        st.markdown(f"""
        <style>
        {style}
        </style>
        """, unsafe_allow_html=True)

        # header
        headerui()

        # layout
        cols = st.columns([0.2, 2, 0.1, 2, 0.1, 5, 0.2])
        with cols[1]:
            signalsPanel()
        with cols[3]:
            operationsPanel()
        with cols[5]:
            signalGraph()

    def show_error(self, errorMessage):
        st.error(errorMessage)
