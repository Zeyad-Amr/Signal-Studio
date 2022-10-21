from signal import signal
import streamlit as st
from matplotlib import pyplot as plt
import numpy as np


class centerSignalView:
    def __init__(self):
        with open("./styles/style.css") as source:
            style = source.read()

        st.markdown(f"""
        <style>
        {style}
        </style>
        """, unsafe_allow_html=True)

        self.fig, self.ax = plt.subplots()

        if 'figureSpot' not in st.session_state:
            self.figureSpot = st.pyplot(self.fig)
            st.session_state.figureSpot = self.figureSpot

    def draw_signal(self):
        signal = st.session_state.signal
        plt.style.use(
            "https://raw.githubusercontent.com/dhaitz/matplotlib-stylesheets/master/pitayasmoothie-dark.mplstyle")
        self.ax.plot(signal.iloc[:, 0], signal.iloc[:, 1], color="#5891C7")

        self.ax.set_title("Signal Digram.")
        self.ax.set_xlabel("time")
        self.ax.set_ylabel("Amplitude")

        with st.session_state.figureSpot:
            st.pyplot(self.fig)


    def draw_signal_with_noise(self):
        signal = st.session_state.signalWithNoise
        plt.style.use(
            "https://raw.githubusercontent.com/dhaitz/matplotlib-stylesheets/master/pitayasmoothie-dark.mplstyle")
        self.ax.plot(signal.iloc[:, 0], signal.iloc[:, 1], color="#5891C7")

        self.ax.set_title("Signal with Noise Digram.")
        self.ax.set_xlabel("time")
        self.ax.set_ylabel("Amplitude")

        with st.session_state.figureSpot:
            st.pyplot(self.fig)


    def draw_sampled_signal(self):
        sampledSignal = st.session_state.sampledSignal

        self.ax.scatter(sampledSignal.iloc[:, 0], sampledSignal.iloc[:, 1])
        
        with st.session_state.figureSpot:
            st.pyplot(self.fig)

    def error_occur(self):
        self.fig, self.ax = plt.subplots()
        with st.session_state.figureSpot:
            st.pyplot(self.fig)
