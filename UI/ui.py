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
        # .....testing add_signal & generate_signal functions
        # amplitude1=1
        # frequency1=1
        # phase1=0
        # sampleRate1=100 
        # time1=np.arange(0, 10, 1/sampleRate1)
        # y1=amplitude1* np.sin(2*np.pi*frequency1*time1+ phase1)
        # d1 = {'t': time1, 'y': y1}
        # signal1 = pd.DataFrame(data=d1)
        # amplitude2=1
        # frequency2=1
        # phase2=0
        # sampleRate2=100 
        # time2=np.arange(0, 10, 1/sampleRate2)
        # y=amplitude2* np.sin(2*np.pi*frequency2*time2+ phase2)
        # d2 = {'t': time2, 'y': y}
        # signal2 = pd.DataFrame(data=d2)
        # st.button("Add", on_click=self.add_signal(signal1, signal2))
        # st.button("Generate", on_click=self.generate_signal)





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
    
    
    def add_signal(self, signal1, signal2):
        if(signal1['t'].equals(signal2['t'])):
            mixedd={'t': signal1['t'], 'y': signal1['y']+signal1['y']}
            mixedSignal=pd.DataFrame(data=mixedd)
            self.draw_signal(mixedSignal)
        else:
            raise ValueError(
                "The Input signals Can't be plotted.")

