import streamlit as st
import pandas as pd
import numpy as np
from UI.center_signal_view import centerSignalView

class headerUI:
    def __init__(self):
        with open("./styles/style.css") as source:
            style = source.read()

        # Removing Streamlit hamburger and footer.
        st.markdown(f"""
        <style>
        {style}
        </style>
        """, unsafe_allow_html=True)

        headerCols = st.columns([2, 2.5, 2.5, 2.5,10,2, 2.5, 3])
        
        if 'sideNav' not in st.session_state:
            st.session_state['sideNav'] = 0

        with headerCols[1]:
            st.button('Add Signal', key="AddSignalButton")

        with headerCols[2]:
            st.button('Add Noise', key="AddNoiseButton")

        with headerCols[3]:
            st.button('Sampling', key="SamplingButton")

        with headerCols[6]:
             st.button('Delete', key="deleteSignalsButton")

        
        if st.session_state.AddNoiseButton:
            st.session_state.graphWidget.error_occur()
            st.session_state.sideNav = 1

        if st.session_state.SamplingButton:
            st.session_state.graphWidget.error_occur()
            st.session_state.sideNav = 0

        if st.session_state.deleteSignalsButton:
            st.session_state.graphWidget.error_occur()
            st.session_state.sideNav = 3
            


        with headerCols[7]:
            st.download_button(label='Export', mime='text/csv', file_name=st.session_state.fileToDownloadName + '.csv',
                               data=st.session_state.fileToDownload, key="ExportButton")
