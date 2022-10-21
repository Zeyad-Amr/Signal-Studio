from logging import PlaceHolder
import os
from pathlib import Path
from typing_extensions import Self
import streamlit as st
from matplotlib import pyplot as plt
from werkzeug.utils import secure_filename
from data_processing import processing
import streamlit as st
import numpy as np
import pandas as pd


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

        st.file_uploader(label="Upload Your Signal File:", type=['csv'],
                        on_change=self.change_signal_upload, key="signalUploader")

        st.slider(label="Change your samlping rate: ", min_value=0, max_value=100,
                        on_change=self.change_sampling_rate, key="signalSlider")
        

    def change_signal_upload(self):
        try:
            filePath = self.save_file(st.session_state.signalUploader)
            self.start_signal_drawing(filePath)
        except Exception as errorMessage:
            self.show_error(errorMessage)

        # st.download_button(label="Save Signal", data = st.session_state.signal.outputFile, file_name=self.signalObject.outputFileName,
        #     mime = 'csv', key="downloadButton")

    def save_file(self, csvFile):
        filePath = os.path.join(
            Path(__file__).parent.parent, 'uploads', secure_filename(csvFile.name))

        with open(filePath, "wb") as file:
            file.write(csvFile.getbuffer())

        return filePath

    def start_signal_drawing(self, filePath):
        try:
            self.signalObject.reading_signal(filePath)
            self.draw_signal(self.signalObject.signal)
            st.session_state.signal = self.signalObject

        except Exception as errorMessage:
            self.show_error(errorMessage)

    def change_sampling_rate(self):
        try:
            self.reconstruct_signal()
            # st.session_state.signal.sample_signal()
            # TODO: Sampling then Drawing
           # st.write(st.session_state.signal.signal)

            self.draw_signal(st.session_state.signal.signal)
        except Exception as errorMessage:
            self.show_error(errorMessage)

    def reconstruct_signal(self):
        f = 20
        t = st.session_state.signal.signal.iloc[:, 0]
        x1 = np.sinc(2 * np.pi * f * t)
        sampleRate = st.session_state.signalSlider
        T = 1/sampleRate
        n = np.arange(0, 0.5 / T)
        nT = n * T
        d = {'t': t, 'x1': x1}

        signal = pd.DataFrame(data=d)
        self.draw_signal(signal)

    def draw_signal(self, signal):
        try:

            fig, ax = plt.subplots()

            ax.plot(signal.iloc[:, 0], signal.iloc[:, 1])
            ax.set_title("Signal Digram.")
            ax.set_xlabel("time")
            ax.set_ylabel("Amplitude")
            ax.grid(True)
            st.pyplot(fig)
        except:
            raise ValueError(
                "The Input Data isn't a signal, and Can't be plotted.")

    def show_error(self, errorMessage):
        st.error(errorMessage)
    
    def generate_signal(self):
        amplitude=1
        frequency=1
        phase=0
        sampleRate=100 
        time=np.arange(0, 10, 1/sampleRate)
        y=amplitude* np.sin(2*np.pi*frequency*time+ phase)
        d = {'t': time, 'y': y}

        signal = pd.DataFrame(data=d)
        self.draw_signal(signal)
    
    
    def add_signal(self, firstSignal, secondSignal):
        if(firstSignal['t'].equals(secondSignal['t'])):
            outputSignal={'t': firstSignal['t'], 
                    'y': firstSignal['y'] + secondSignal['y']}

            outputDataFrame = pd.DataFrame(outputSignal)
            return(outputDataFrame)
        else:
            raise ValueError(
                "The Input signals Can't be plotted.")

