import streamlit as st
from dataProcessing import processing
import pandas as pd
import plotly.graph_objects as go
import os
from pathlib import Path
from werkzeug.utils import secure_filename


class stateManagement:
    def __init__(self):

        if 'signals' not in st.session_state:
            st.session_state.signals = []

        if 'generatedSignals' not in st.session_state:
            st.session_state.generatedSignals = []

        if 'sampledSignal' not in st.session_state:
            st.session_state.sampledSignal = pd.DataFrame({})

        if 'signalObject' not in st.session_state:
            self.signalObject = processing.SignalProcessing()
            st.session_state.signalObject = self.signalObject

        if 'fileToDownload' not in st.session_state:
            st.session_state.fileToDownload = pd.DataFrame().to_csv(index=False).encode('utf-8')

        if 'fileToDownloadName' not in st.session_state:
            st.session_state.fileToDownloadName = "Untitled"

        if 'recCounter' not in st.session_state:
            st.session_state.recCounter = 0

        if 'mixCounter' not in st.session_state:
            st.session_state.mixCounter = 0

        if 'signalCounter' not in st.session_state:
            st.session_state.signalCounter = 0

        if 'generatedSignalCounter' not in st.session_state:
            st.session_state.generatedSignalCounter = 0

        if 'viewDeletePanel' not in st.session_state:
            st.session_state.viewDeletePanel = False

        if "sampling_slider" not in st.session_state:
            st.session_state["sampling_slider"] = 0

        if "SNR_slider" not in st.session_state:
            st.session_state["SNR_slider"] = 0

        if "exportNameKey" not in st.session_state:
            st.session_state["exportNameKey"] = ""

        if 'signalCounter' not in st.session_state:
            st.session_state.signalCounter = 0

        if 'generatedSignalCounter' not in st.session_state:
            st.session_state.generatedSignalCounter = 0

################### Start Draw Signal Graph Function #################

    def draw_signal(self):
        self.fig = go.Figure()
        signal = st.session_state.signal
        self.fig.add_trace(go.Scatter(
            x=signal.iloc[:, 0],
            y=signal.iloc[:, 1],
            mode='lines',
            name='lines'))

        self.fig.update_layout(title="Signal Digram.",
                               xaxis_title="time",
                               yaxis_title="Amplitude")

        self.fig.update_xaxes(showgrid=False, automargin=True)
        self.fig.update_yaxes(showgrid=False, automargin=True)

        self.fig.update_layout(
            height=450,
            margin={
                'l': 0,
                'r': 0,
                'b': 0,
                't': 0
            }
        )

        with st.session_state.figureSpot:
            st.plotly_chart(self.fig, use_container_width=True)

    ################### End Draw Signal Graph Function #################

    ################### Start Draw Noised Signal Graph Function #################

    def draw_signal_with_noise(self):
        self.fig = go.Figure()
        signal = st.session_state.signalWithNoise

        self.fig.add_trace(go.Scatter(
            x=signal.iloc[:, 0],
            y=signal.iloc[:, 1],
            mode='lines',
            name='dots'))

        self.fig.update_layout(title="Signal with Noise Digram.",
                               xaxis_title="time",
                               yaxis_title="Amplitude")

        self.fig.update_xaxes(showgrid=False, automargin=True)
        self.fig.update_yaxes(showgrid=False, automargin=True)

        self.fig.update_layout(
            height=450,
            margin={
                'l': 0,
                'r': 0,
                'b': 0,
                't': 0
            }
        )

        with st.session_state.figureSpot:
            st.plotly_chart(self.fig, use_container_width=True)
    ################### End Draw Noised Signal Graph Function #################

    ################### Start Draw Sampled Signal Graph Function #################

    def draw_sampled_signal(self):
        self.fig = go.Figure()
        sampledSignal = st.session_state.sampledSignal
        signal = st.session_state.signal

        self.fig.add_trace(go.Scatter(
            x=signal.iloc[:, 0],
            y=signal.iloc[:, 1],
            mode='lines',
            name='signal'))

        self.fig.add_trace(go.Scatter(
            x=sampledSignal.iloc[:, 0],
            y=sampledSignal.iloc[:, 1],
            mode='markers',
            name='sampled signal'))

        self.fig.update_layout(legend={})
        self.fig.update_xaxes(showgrid=False, automargin=True)
        self.fig.update_yaxes(showgrid=False, automargin=True)

        self.fig.update_layout(title="Sampled Signal Digram.",
                               xaxis_title="time",
                               yaxis_title="Amplitude")

        self.fig.update_layout(
            height=450,
            margin={
                'l': 0,
                'r': 0,
                'b': 0,
                't': 0
            }
        )

        with st.session_state.figureSpot:
            st.plotly_chart(self.fig, use_container_width=True)
    ################### End Draw Sampled Signal Graph Function #################

    ################### Start Draw Empty Graph Graph Function #################

    def draw_empty_graph(self):
        self.fig = go.Figure()
        self.fig.update_xaxes(showgrid=False, automargin=True)
        self.fig.update_yaxes(showgrid=False, automargin=True)
        self.fig.update_layout(
            height=450,
            margin={
                'l': 0,
                'r': 0,
                'b': 0,
                't': 0
            }
        )
        with st.session_state.figureSpot:
            st.plotly_chart(self.fig, use_container_width=True)

    ################### End Draw Empty Graph Function #################

    ################### Start onChange Function #################

    def on_change(self):
        try:
            for signal in st.session_state.signals:
                if signal['name'] == st.session_state.selectedSignal:
                    st.session_state.signal = signal['signal']

                    self.draw_signal()
                    st.session_state.fileToDownload = signal['signal'].to_csv(
                        index=False).encode('utf-8')
                    st.session_state.fileToDownloadName = signal['name']
        except:
            self.draw_empty_graph()
            st.error("Can't Import this signal...")

    ################### End onChange Function #################

    ################### Start Add Signal Function #################

    def add_signal(self, signalDict):
        st.session_state.signals.insert(0, signalDict)
        st.session_state.signal = signalDict['signal']
        st.session_state.selectedSignal = signalDict['name']

    ################### End onChange Function #################

    ################### Start Save File Function #################

    def save_file(self, csvFile):
        try:
            filePath = os.path.join(
                Path(__file__).parent.parent, 'uploads', secure_filename(csvFile.name))

            with open(filePath, "wb") as file:
                file.write(csvFile.getbuffer())

            return filePath
        except:
            raise ValueError("Can't Upload this file, please try again...")

    ################### End Save File Function #################

    ################### Start Delete Signal Function #################

    def delete_signals(self, signalsNames):
        try:
            remaningSignals = []
            for signal in st.session_state.signals:
                isExist = False
                for deletedSignal in signalsNames:
                    if signal['name'] == deletedSignal:
                        isExist = True
                if not isExist:
                    remaningSignals.append(signal)

            st.session_state.signals = remaningSignals
            st.session_state.viewDeletePanel = False

        except:
            self.show_error("Can't Delete this signals.")

    ################### End Delete Signal Function #################

    ################### Start Generate Signal Function #################

    def add_generated_signal_name(self, sObject):
        for i in st.session_state.generatedSignals:
            if i['name'] == sObject['name']:
                flag = False
                sObject['name'] = sObject['name'] + \
                    ' {}'.format(st.session_state.generatedSignalCounter)
                st.session_state.generatedSignalCounter += 1
                break
        st.session_state.generatedSignals.append(sObject)
    ################### End Generate Signal Function #################
