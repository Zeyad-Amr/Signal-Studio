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

        headerCols = st.columns([2, 2, 2, 2, 2, 2,8, 1, 2])

        with headerCols[1]:
            st.button('Add Signal', key="AddSignalButton")

        with headerCols[2]:
            st.button('Add Noise', key="AddNoiseButton")

        with headerCols[3]:
            st.button('Sampling', key="SamplingButton")

        with headerCols[4]:
            st.button('Clear', key="ClearButton")

        with headerCols[5]:
            if not st.session_state.viewDeletePanel:
                st.button('Delete', key="deleteSignalsButton")
                if st.session_state.deleteSignalsButton:
                    st.session_state.viewDeletePanel = True
            else:
                st.button('Signals', key="ViewSignalsButton")
                if st.session_state.ViewSignalsButton:
                    st.session_state.viewDeletePanel = False
        with headerCols[6]:
            if st.session_state.ffff:
                st.write("ffff")
        with headerCols[7]:
            st.download_button(label='Export', mime='csv', file_name=st.session_state.fileToDownloadName,
                               data=st.session_state.fileToDownload, key="ExportButton")

        if st.session_state.AddSignalButton:
            self.add_button()

        if st.session_state.AddNoiseButton:
            self.add_noise()

        if st.session_state.ClearButton:
            st.session_state.graphWidget.error_occur()
            st.session_state.signal = pd.DataFrame()

