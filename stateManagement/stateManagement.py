import streamlit as st
from dataProcessing.processing import SignalProcessing
import pandas as pd
import plotly.graph_objects as go
import os
from pathlib import Path
from werkzeug.utils import secure_filename


class stateManagement:
    def __init__(self):

        if 'currentSignal' not in st.session_state:
            st.session_state.currentSignal = {
                'name':'',
                'signal':pd.DataFrame({})
            }

        if 'signalsList' not in st.session_state:
            st.session_state.signalsList = []

        if 'pureSignal' not in st.session_state:
            st.session_state.pureSignal = {
                'name':'',
                'signal':pd.DataFrame({})
            }

        if 'sampledSignal' not in st.session_state:
            st.session_state.sampledSignal = {
                'name':'',
                'signal':pd.DataFrame({})
            }

        if 'reconstructedSignal' not in st.session_state:
            st.session_state.reconstructedSignal = {
                'name':'',
                'signal':pd.DataFrame({})
            }


        if 'isGenerateMode' not in st.session_state:
            st.session_state.isGenerateMode = True

        # if 'signals' not in st.session_state:
        #     st.session_state.signals = []

        # if 'generatedSignals' not in st.session_state:
        #     st.session_state.generatedSignals = []

        # if 'sampledSignal' not in st.session_state:
        #     st.session_state.sampledSignal = pd.DataFrame({})

        # if 'signalObject' not in st.session_state:
        #     self.signalObject = processing.SignalProcessing()
        #     st.session_state.signalObject = self.signalObject

        # if 'fileToDownload' not in st.session_state:
        #     st.session_state.fileToDownload = pd.DataFrame().to_csv(index=False).encode('utf-8')

        # if 'fileToDownloadName' not in st.session_state:
        #     st.session_state.fileToDownloadName = "Untitled"

        # if 'recCounter' not in st.session_state:
        #     st.session_state.recCounter = 0

        # if 'mixCounter' not in st.session_state:
        #     st.session_state.mixCounter = 0

        # if 'signalCounter' not in st.session_state:
        #     st.session_state.signalCounter = 0

        # if 'generatedSignalCounter' not in st.session_state:
        #     st.session_state.generatedSignalCounter = 0

        # if 'viewDeletePanel' not in st.session_state:
        #     st.session_state.viewDeletePanel = False

        # if "sampling_slider" not in st.session_state:
        #     st.session_state["sampling_slider"] = 0

        # if "SNR_slider" not in st.session_state:
        #     st.session_state["SNR_slider"] = 0

        # if "exportNameKey" not in st.session_state:
        #     st.session_state["exportNameKey"] = ""

        # if 'signalCounter' not in st.session_state:
        #     st.session_state.signalCounter = 0

        # if 'generatedSignalCounter' not in st.session_state:
        #     st.session_state.generatedSignalCounter = 0

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

    def set_generated_signal(self, amp, freq, phase):
        processing = SignalProcessing()
        generatedSignal = processing.generate_signal(
            amplitude=amp, frequency=freq, phase=phase)
        signal = {
            'name': 'Signal' + ' {}'.format(len(st.session_state.signalsList)+1),
            'signal': generatedSignal
        }
        st.session_state.pureSignal = signal

################### End Generate Signal Function #################

################### Start Upload Signal Function #################

    def set_uploaded_signal(self, path):
        processing = SignalProcessing()
        uploadedSignal = processing.reading_signal(path)
        st.session_state.pureSignal = uploadedSignal

################### End Upload Signal Function #################

################### Start Draw Noised Signal Graph Function #################

    def set_noised_signal(self, snr):
        processing = SignalProcessing()

        st.session_state.currentSignal = {
            'name':st.session_state.pureSignal['name'],
            'signal': processing.add_noise( signal=st.session_state.pureSignal['signal'], SNR=snr)
        }

################### End Draw Noised Signal Graph Function #################

################### Start Draw Sampled Signal Graph Function #################

    def set_sampled_signal(self, sampleRate):
        processing = SignalProcessing()
        st.session_state.sampledSignal = {
            'name':'Sample',
            'signal': processing.sample_signal( signal=st.session_state.pureSignal['signal'], 
                                                sampleRate=sampleRate)
        }

################### End Draw Sampled Signal Graph Function #################

################### Start Draw Signal Graph Function #################

    # def draw_signal(self):
    #     self.fig = go.Figure()
    #     signal = st.session_state.signal
    #     self.fig.add_trace(go.Scatter(
    #         x=signal.iloc[:, 0],
    #         y=signal.iloc[:, 1],
    #         mode='lines',
    #         name='lines'))

    #     self.fig.update_layout(title="Signal Digram.",
    #                            xaxis_title="time",
    #                            yaxis_title="Amplitude")

    #     self.fig.update_xaxes(showgrid=False, automargin=True)
    #     self.fig.update_yaxes(showgrid=False, automargin=True)

    #     self.fig.update_layout(
    #         height=450,
    #         margin={
    #             'l': 0,
    #             'r': 0,
    #             'b': 0,
    #             't': 0
    #         }
    #     )

    #     with st.session_state.figureSpot:
    #         st.plotly_chart(self.fig, use_container_width=True)

    ################### End Draw Signal Graph Function #################

    ################### Start Draw Empty Graph Graph Function #################

    # def draw_empty_graph(self):
    #     self.fig = go.Figure()
    #     self.fig.update_xaxes(showgrid=False, automargin=True)
    #     self.fig.update_yaxes(showgrid=False, automargin=True)
    #     self.fig.update_layout(
    #         height=450,
    #         margin={
    #             'l': 0,
    #             'r': 0,
    #             'b': 0,
    #             't': 0
    #         }
    #     )
    #     with st.session_state.figureSpot:
    #         st.plotly_chart(self.fig, use_container_width=True)

    ################### End Draw Empty Graph Function #################
