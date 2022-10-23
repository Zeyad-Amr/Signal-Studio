from matplotlib.style import use
import streamlit as st
from matplotlib import pyplot as plt
import numpy as np
import plotly.graph_objects as go

class centerSignalView:
    def __init__(self):
        with open("./styles/style.css") as source:
            style = source.read()

        st.markdown(f"""
        <style>
        {style}
        </style>
        """, unsafe_allow_html=True)


        self.fig = go.Figure()
        self.fig.update_layout(
            height = 450,
            margin = {
                'l':0,
                'r':0,
                'b':0,
                't':0
            }
        )
        self.fig.update_xaxes(showgrid = False, automargin=True)
        self.fig.update_yaxes(showgrid = False, automargin=True)
        if 'figureSpot' not in st.session_state:
            self.figureSpot = st.plotly_chart(self.fig, use_container_width=True)
            st.session_state.figureSpot = self.figureSpot

    def draw_signal(self):
        self.fig = go.Figure()
        signal = st.session_state.signal
        self.fig.add_trace(go.Scatter(
            x = signal.iloc[:, 0],
            y=signal.iloc[:, 1], 
            mode='lines',
            name='lines'))

        self.fig.update_layout(title = "Signal Digram.", 
                                xaxis_title = "time", 
                                yaxis_title="Amplitude")

        self.fig.update_xaxes(showgrid = False, automargin=True)
        self.fig.update_yaxes(showgrid = False, automargin=True)
        
        self.fig.update_layout(
            height = 450,
            margin = {
                'l':0,
                'r':0,
                'b':0,
                't':0
            }
        )

        with st.session_state.figureSpot:
            st.plotly_chart(self.fig, use_container_width=True)

    def draw_signal_with_noise(self):
        self.fig = go.Figure()
        signal = st.session_state.signalWithNoise

        self.fig.add_trace(go.Scatter(
            x = signal.iloc[:, 0],
            y=signal.iloc[:, 1],
            mode='lines',
            name='dots'))


        self.fig.update_layout(title = "Signal with Noise Digram.", 
                                xaxis_title = "time", 
                                yaxis_title="Amplitude")

        self.fig.update_xaxes(showgrid = False, automargin=True)
        self.fig.update_yaxes(showgrid = False, automargin=True)
        
        self.fig.update_layout(
            height = 450,
            margin = {
                'l':0,
                'r':0,
                'b':0,
                't':0
            }
        )

        with st.session_state.figureSpot:
            st.plotly_chart(self.fig, use_container_width=True)

    def draw_sampled_signal(self):
        self.fig = go.Figure()
        sampledSignal = st.session_state.sampledSignal
        signal = st.session_state.signal

        self.fig.add_trace(go.Scatter(
            x = signal.iloc[:, 0],
            y= signal.iloc[:, 1],
            mode='lines',
            name='signal'))

        self.fig.add_trace(go.Scatter(
            x = sampledSignal.iloc[:, 0],
            y=sampledSignal.iloc[:, 1],
            mode='markers',
            name='sampled signal'))

        self.fig.update_layout(legend = {})
        self.fig.update_xaxes(showgrid = False, automargin=True)
        self.fig.update_yaxes(showgrid = False, automargin=True)

        self.fig.update_layout(title = "Sampled Signal Digram.", 
                                xaxis_title = "time", 
                                yaxis_title="Amplitude")

        self.fig.update_layout(
            height = 450,
            margin = {
                'l':0,
                'r':0,
                'b':0,
                't':0
            }
        )

        with st.session_state.figureSpot:
            st.plotly_chart(self.fig, use_container_width=True)

    def error_occur(self):
        self.fig = go.Figure()
        self.fig.update_xaxes(showgrid = False, automargin=True)
        self.fig.update_yaxes(showgrid = False, automargin=True)
        self.fig.update_layout(
            height = 450,
            margin = {
                'l':0,
                'r':0,
                'b':0,
                't':0
            }
        )
        with st.session_state.figureSpot:
            st.plotly_chart(self.fig, use_container_width=True)
