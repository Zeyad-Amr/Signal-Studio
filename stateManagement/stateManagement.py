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
                'name': '',
                'signal': pd.DataFrame({})
            }

        if 'signalsList' not in st.session_state:
            st.session_state.signalsList = []

        if 'pureSignal' not in st.session_state:
            st.session_state.pureSignal = {
                'name': '',
                'signal': pd.DataFrame({})
            }
            self.set_generated_signal(phase = 0, amp=1, freq=1)

        if 'sampledSignal' not in st.session_state:
            st.session_state.sampledSignal = {
                'name': '',
                'signal': pd.DataFrame({})
            }

        if 'reconstructedSignal' not in st.session_state:
            st.session_state.reconstructedSignal = {
                'name': '',
                'signal': pd.DataFrame({})
            }

        if 'Mode' not in st.session_state:
            st.session_state.Mode = 0

        if 'signalView' not in st.session_state:
            st.session_state.signalView = True

        if 'sampleView' not in st.session_state:
            st.session_state.sampleView = True

        if 'reconstructedview' not in st.session_state:
            st.session_state.reconstructedview = True

        if 'selectedSignals' not in st.session_state:
            st.session_state.selectedSignals = []


################### Start Add Signal Function #################

    def save_signal(self):
        st.session_state.signalsList.insert(0, st.session_state.currentSignal)

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

    def delete_signals(self, signals):

        remaningSignals = []
        for signal in st.session_state.signalsList:
            isExist = False
            for deletedSignal in signals:
                if signal['name'] == deletedSignal['name']:
                    isExist = True
            if not isExist:
                remaningSignals.append(signal)

        st.session_state.signalsList = remaningSignals
        st.experimental_rerun()


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
            'name': st.session_state.pureSignal['name'],
            'signal': processing.add_noise(signal=st.session_state.pureSignal['signal'], SNR=snr)
        }

################### End Draw Noised Signal Graph Function #################

################### Start Draw Sampled Signal Graph Function #################

    def set_sampled_signal(self, sampleRate):
        processing = SignalProcessing()
        st.session_state.sampledSignal = {
            'name': 'Sample',
            'signal': processing.sample_signal(signal=st.session_state.pureSignal['signal'],
                                               sampleRate=sampleRate)
        }

################### End Draw Sampled Signal Graph Function #################

# Start

    def set_reconstructed_signal(self):
        processing = SignalProcessing()
        st.session_state.reconstructedSignal = {
            'name': 'Sample',
            'signal': processing.reconstruct_signal(st.session_state.sampledSignal['signal'])
        }

    def set_add_signals(self):
        processing = SignalProcessing()
        if len(st.session_state.selectedSignals) != 0:
            if len(st.session_state.selectedSignals) == 1:
                st.session_state.pureSignal = st.session_state.selectedSignals[0]
            else:
                st.session_state.pureSignal = processing.add_signals(
                    st.session_state.selectedSignals)

# END
