import os
from pathlib import Path
import streamlit as st
from werkzeug.utils import secure_filename
from data_processing.files_handling import reading_signal


class AppUi:
    def __init__(self):
        st.set_page_config(page_title='Sampling Studio')

        # Removing Streamlit hamburger and footer.
        st.markdown("""
        <style>
            .css-9s5bis.edgvbvh3 {
                visibility : hidden;
            }
            .css-1q1n0ol.egzxvld0 {
                visibility : hidden;
            }
        </style>
        """, unsafe_allow_html=True)

        st.file_uploader(label = "Upload Your Signal File:", type=['csv'],
            on_change=self.change_signal_upload, key="signalUploader")

        st.slider(label="Change your samlping rate: ", min_value= 0, max_value=100, \
            on_change=self.change_sampling_rate, key="signalSlider")

    def change_signal_upload(self):
        filePath = self.save_file(st.session_state.signalUploader)
        self.start_signal_drawing(filePath)

    def save_file(self, csvFile):
        filePath = os.path.join(
            Path(__file__).parent.parent, 'uploads', secure_filename(csvFile.name))

        with open(filePath, "wb") as file: 
            file.write(csvFile.getbuffer())

        return filePath

    def start_signal_drawing(self, filePath):
        self.signalDataFrame = reading_signal(filePath)
        # TODO: Signal Sampling and Signal Drawing.
        
    def change_sampling_rate(self):
        # TODO: Sampling Controll.
        print(st.session_state.signalSlider)

