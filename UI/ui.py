import dis
import os
from pathlib import Path
import streamlit as st
import plotly.figure_factory as ff
from werkzeug.utils import secure_filename
from data_processing import processing


class AppUi:
    def __init__(self):
        self.signalObject = processing.SignalProcessing()
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

        st.slider(label="Change your samlping rate: ", min_value= 0, max_value=100,
            on_change=self.change_sampling_rate, key="signalSlider")

    def show_error(self, errorMessage):
        st.error(errorMessage)
        

    def change_signal_upload(self):
        filePath = self.save_file(st.session_state.signalUploader)
        self.start_signal_drawing(filePath)

        st.download_button(label="Save Signal", on_click=self.signalObject.saving_signal, data = self.signalObject.outputFile, 
            file_name=self.signalObject.outputFileName, mime = 'csv', key="downloadButton")
    
       

    def save_file(self, csvFile):
        filePath = os.path.join(
            Path(__file__).parent.parent, 'uploads', secure_filename(csvFile.name))

        with open(filePath, "wb") as file: 
            file.write(csvFile.getbuffer())

        return filePath

    def start_signal_drawing(self, filePath):
        try:
            self.signalObject.reading_signal(filePath)
            # self.sampledSignal = self.signalObject.sample_signal()
            # TODO: Signal Drawing. 
        except Exception as exceptionMessage:
            self.show_error(exceptionMessage)
        
    def change_sampling_rate(self):
        self.sampledSignal = self.signalObject.sample_signal(st.session_state.signalSlider)
        # TODO: Signal Drawing.

    def draw_signal(self, signalDataFrame):
        fig = ff.create_distplot(signalDataFrame, bin_size=[.1, .25, .5])
        st.plotly_chart(fig, use_container_width=True)