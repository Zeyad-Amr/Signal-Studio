import streamlit as st
import pandas as pd
import numpy as np


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

        headerCols = st.columns([2, 2, 2, 2, 2, 10, 1, 2])

        if 'fileToDownload' not in st.session_state:
            st.session_state.fileToDownload = pd.DataFrame({'t':[], 'y':[]}).to_csv(index=False).encode('utf-8')
        if 'fileToDownloadName' not in st.session_state:
            st.session_state.fileToDownloadName = "Untitled"

        with headerCols[1]:
            st.button('Add Signal', key="AddSignalButton")
        with headerCols[2]:
            st.button('Add Noise', key="AddNoiseButton")
        with headerCols[3]:
            st.button('Sampling', key="SamplingButton")
        with headerCols[4]:
            st.button('Clear', key="ClearButton")
        with headerCols[6]:
            st.download_button(label='Export', mime='csv', file_name = st.session_state.fileToDownloadName, 
                data = st.session_state.fileToDownload, key="ExportButton")
    
        if st.session_state.AddSignalButton:
            self.add_button()

        if st.session_state.AddNoiseButton:
            self.add_noise()

        if st.session_state.ClearButton:
            st.session_state.pop('signal')
            st.session_state.graphWidget.error_occur()


    


    
