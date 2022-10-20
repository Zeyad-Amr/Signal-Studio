from logging import PlaceHolder
import os
from pathlib import Path
from time import time
from requests import session
import streamlit as st
from matplotlib import pyplot as plt
from werkzeug.utils import secure_filename
from data_processing import processing
from UI.header import headerUI
from UI.left_navbar import leftNavBar
from UI.right_navbar import rightNavBar
from UI.center_signal_view import centerSignalView
import numpy as np
import pandas as pd
import sys


class AppUi:
    def __init__(self):

        self.signalObject = processing.SignalProcessing()

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
        x = headerUI()

        st.write("---")

        # layout
        cols = st.columns([0.1, 1, 0.1, 2, 0.1, 1, 0.1])
        with cols[1].container():
            leftNavBar()
        with cols[3].container():
            centerSignalView()
        with cols[5].container():
            rightNavBar()

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
            # self.reconstruct_signal()
            # st.session_state.signal.sample_signal()
            # TODO: Sampling then Drawing
            self.sample_signal()
            # st.write(st.session_state.signal.signal)

            self.draw_signal(st.session_state.signal.signal)
        except Exception as errorMessage:
            self.show_error(errorMessage)

    def sample_signal(self):
        try:
            sampleRate = st.session_state.signalSlider
            t = st.session_state.signal.signal.iloc[:, 0]
            y = st.session_state.signal.signal.iloc[:, 1]

            freqs = np.fft.fftfreq(len(t))
            maxFrequency = np.max(freqs)

            # guard class for freq
            # BUG  # error catch should be handled to catch this message instead of throw (can't sample the function)
            if sampleRate < (2 * maxFrequency) or sampleRate > t.shape[0]:
                raise ValueError('Sample Rate isn''t enough')

            step = t.shape[0] // sampleRate
            timeArray = []
            amplitudeArray = []
            i = 0

            while (i < t.shape[0]):
                timeArray.append(t[i])
                amplitudeArray.append(y[i])
                i += step
                i = int(i)
            d = {'t': timeArray, 'y': amplitudeArray}
            signal = pd.DataFrame(data=d)
            self.reconstruct_signal(signal)
        except:
            raise ValueError("Can't sample the function")

    def reconstruct_signal(self, signal):
        t = signal.iloc[:, 0]
        y = signal.iloc[:, 1]
        for i in range(t.shape[0]):
            if t[i] < 0:
                y[i] = 0
        y = self.yRe(t, y)
        d = {'t': t, 'y': y}
        signal = pd.DataFrame(data=d)
        self.draw_signal(signal)

    def yRe(self, t, y):
        Ts = t[2] - t[1]
        fs = 1 / Ts
        st.write(fs)
        z = 0
        for i in range(-int((t.shape[0] - 1) / 2), int((t.shape[0] - 1) / 2), 1):
            n = int(i + (t.shape[0] - 1) / 2 + 1)
            z += y[n] * np.sin(np.pi * fs * (t - i * Ts)) / (np.pi * fs * (t - i * Ts))
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
            raise ValueError(
                "The Input Data isn't a signal, and Can't be plotted.")

    def draw_sampled_signal(self, signal):
        try:

            fig, ax = plt.subplots()

            ax.plot(signal.iloc[:, 0], signal.iloc[:, 1], 'r-')
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
