from asyncio.windows_events import NULL
from logging import PlaceHolder
import os
from pathlib import Path
from time import time
from requests import session
import streamlit as st
from matplotlib import pyplot as plt
from werkzeug.utils import secure_filename
from data_processing import processing
import streamlit as st
import numpy as np
import pandas as pd


class AppUi:
    def __init__(self):
        st.session_state.signals = []
        st.session_state.noises = []
        st.session_state.sampledSignal = pd.DataFrame()

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
                         on_change=self.upload_signal, key="signalUploader")

        st.slider(label="Change your samlping rate: ", min_value=0, max_value=100,
                  on_change=self.sample_signal, key="signalSlider")

    def upload_signal(self):
        try:
            filePath = self.save_file(st.session_state.signalUploader)
            st.session_state.signals.append(self.signalObject.reading_signal(filePath))
        except Exception as errorMessage:
            self.show_error(errorMessage)
    
    def save_file(self, csvFile):
        try:
            filePath = os.path.join(
                Path(__file__).parent.parent, 'uploads', secure_filename(csvFile.name))

            with open(filePath, "wb") as file:
                file.write(csvFile.getbuffer())

            return filePath
        except:
            raise ValueError("Can't Upload this file, please try again...")

    def delete_signal(self, signalName):
        try:
            for signal in range(len(st.session_state.signals)):
                if(st.session_state.signals[signal]['name'] == signalName):
                    st.session_state.signals = st.session_state.signals[:signal] + st.session_state.signals[signal+1:]
            
            self.show_error("Please select signal to delete.")
        except:
            self.show_error("Can't Delete this signal.")

    
    def start_signal_drawing(self, filePath):
        try:
            self.draw_signal(self.signalObject.signal)
            st.session_state.signal = self.signalObject

        except Exception as errorMessage:
            self.show_error(errorMessage)

    # def change_sampling_rate(self):
    #     try:
    #         self.reconstruct_signal()
    #         # st.session_state.signal.sample_signal()
    #         # TODO: Sampling then Drawing
    #         self.sample_signal()
    #        # st.write(st.session_state.signal.signal)

    #         self.draw_signal(st.session_state.signal.signal)
    #     except Exception as errorMessage:
    #         self.show_error(errorMessage)

    def sample_signal(self):
        try:
            sampleRate = st.session_state.signalSlider
            selectButtonValue = st.session_state.checkbox

            # TODO: get the specified signal from the file.

            t = st.session_state.signal.signal.iloc[:, 0]
            x1 = np.sinc(2 * np.pi * f * t)
            sampleRate = st.session_state.signalSlider
            T = 1/sampleRate
            n = np.arange(0, 0.5 / T)
            nT = n * T
            d = {'t': t, 'x1': x1}

            freqs = np.fft.fftfreq(len(t))
            maxFrequency = np.max(freqs)

            # guard class for freq
            # BUG  # error catch should be handled to catch this message instead of throw (can't sample the function)
            if sampleRate < (2*maxFrequency) or sampleRate > t.shape[0]:
                raise ValueError('Sample Rate isn''t enough')

            step = t.shape[0]//sampleRate
            timeArray = []
            amplitudeArray = []
            i = 0

            while (i < t.shape[0]):
                timeArray.append(t[i])
                amplitudeArray.append(y[i])
                i += step
                i = int(i)
            d = {'t': timeArray, 'y': amplitudeArray}
            st.session_state.sampledSignal = pd.DataFrame(data=d)
            self.draw_sampled_signal(st.session_state.sampledSignal)
        except:
            raise ValueError("Can't sample this Signal...")

    def reconstruct_signal(self):
        t = st.session_state.sampledSignal.iloc[:,0]
        y = st.session_state.sampledSignal.iloc[:,1]
        for i in range(t.shape[0]):
            if t[i]<0:
                y[i]=0
        y=self.yRe(t, y)        
        d={'t':t,'y':y}
        signal = pd.DataFrame(data=d)
        self.draw_signal(signal)

        
    def yRe(self,t,y):
        Ts = t[2] - t[1]
        fs=1/Ts
        st.write(fs)
        z = 0
        for i in range(-int((t.shape[0]-1)/2), int((t.shape[0]-1)/2), 1):
             n = int(i + (t.shape[0]-1)/2 + 1)
             z += y[n]*np.sin(np.pi*fs*(t - i*Ts))/(np.pi*fs*(t - i*Ts))
        return z
        
    
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
            raise ValueError("The Input Data isn't a signal, and Can't be plotted.")

    def draw_sampled_signal(self, signal):
        try:

            fig, ax = plt.subplots()

            ax.plot(signal.iloc[:, 0], signal.iloc[:, 1],'r-')
            ax.set_title("Signal Digram.")
            ax.set_xlabel("time")
            ax.set_ylabel("Amplitude")
            ax.grid(True)
            
            st.pyplot(fig)
        except:
            raise ValueError("The Input Data isn't a signal, and Can't be plotted.")

    def show_error(self, errorMessage):
        st.error(errorMessage)
