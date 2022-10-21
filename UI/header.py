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

        with headerCols[1]:
            st.button('Add Signal', key="AddSignalButton")
        with headerCols[2]:
            st.button('Add Noise', key="AddNoiseButton")
        with headerCols[3]:
            st.button('Sampling', key="SamplingButton")
        with headerCols[4]:
            st.button('Clear', key="ClearButton")
        with headerCols[6]:
            st.button('Export', key="ExportButton")
    
        if st.session_state.AddSignalButton:
            self.add_button()

        if st.session_state.AddNoiseButton:
            self.add_noise()



    def add_button(self, signalDict):
        st.session_state.signals.append(signalDict)

    def add_noise(self):
        df = pd.read_csv(r"C:\Users\kamel\OneDrive\Documents\GitKraken\Sampling-Studio\uploads\Untitled_spreadsheet_-_Sheet1.csv")

        st.session_state.noises.append({
            "name": np.random.random(),
            "noise": df
        })

    


    
