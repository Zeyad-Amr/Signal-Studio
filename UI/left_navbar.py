from enum import Flag
import os
from pathlib import Path
from click import clear
from numpy import sign
from werkzeug.utils import secure_filename
import streamlit as st
import os


class leftNavBar:
    def __init__(self):
        with open("./styles/style.css") as source:
            style = source.read()
        st.markdown(f"""
        <style>
        {style}
        </style>
        """, unsafe_allow_html=True)

        if 'signalCounter' not in st.session_state:
            st.session_state.signalCounter = 0

        if 'generatedSignalCounter' not in st.session_state:
            st.session_state.generatedSignalCounter = 0

        with st.expander("Add New Signal"):
            uploadTab, generateTab = st.tabs(["Upload", "Generate"])
            with uploadTab:
                with st.form("my-form", clear_on_submit=True):
                    uploadedSignals = st.file_uploader(
                        "Upload Signal", type=["csv"], key='uploadButton', accept_multiple_files=True)
                    submitted = st.form_submit_button("Upload")

                if submitted and uploadedSignals is not None:
                    for signal in uploadedSignals:
                        try:
                            path = self.save_file(signal)
                            siganlDict = st.session_state.signalObject.reading_signal(
                                path)
                            st.session_state.signal = siganlDict['signal']
                            st.session_state.graphWidget.draw_signal()
                            self.add_button(siganlDict)
                        except:
                            st.error("Error Occur with importing of signal...")

            with generateTab:
                with st.form("generate_signal", clear_on_submit=True):
                    st.write("Generate Signal")
                    signalTitle = st.text_input(
                        "Signal Title", placeholder="Please enter the signal title")

                    freqVal = st.number_input("Frequency (HZ)", step=0.25)
                    ampVal = st.number_input("Amplitude", step=0.25)
                    phaseVal = st.number_input("Phase", step=0.25)

                    submitted = st.form_submit_button("Generate")
                    if submitted:
                        try:
                            siganlObject = st.session_state.signalObject.generate_signal(
                                ampVal, freqVal, phaseVal)
                            if signalTitle:
                                sObject = {
                                    "name": signalTitle,
                                    "signal": siganlObject
                                }
                                self.add_button(sObject)
                                self.add_generated_signal_name(sObject)
                            else:
                                sObject = {
                                    "name": "Untitled {}".format(st.session_state.signalCounter),
                                    "signal": siganlObject
                                }
                                self.add_button(sObject)
                                st.session_state.generatedSignals.append(sObject)
                                st.session_state.signalCounter += 1
                            st.success("Generated Successfully")
                        except:
                            st.error("Can't Generate Signal with these values...")

        self.signalsLst = []
        for signal in st.session_state.signals:
            self.signalsLst.append(signal['name'])
        
        st.radio("Signals", self.signalsLst, key="selectedSignal",
                    on_change=self.on_change_radio)

        if st.session_state.selectedSignal:
            self.on_change()


    def on_change_radio(self):
        self.reset_values()

    def on_change(self):
        try:
            for signal in st.session_state.signals:
                if signal['name'] == st.session_state.selectedSignal:
                    st.session_state.signal = signal['signal']
                    st.session_state.graphWidget.draw_signal()
                    st.session_state.fileToDownload = signal['signal'].to_csv(index=False).encode('utf-8')
                    st.session_state.fileToDownloadName = signal['name']
        except:
            st.session_state.graphWidget.error_occur()
            st.error("Can't Import this signal...")


    def save_file(self, csvFile):
        try:
            filePath = os.path.join(
                Path(__file__).parent.parent, 'uploads', secure_filename(csvFile.name))

            with open(filePath, "wb") as file:
                file.write(csvFile.getbuffer())

            return filePath
        except:
            raise ValueError("Can't Upload this file, please try again...")

    def add_button(self, signalDict):
        st.session_state.signals.insert(0, signalDict)
        st.session_state.signal = signalDict['signal']
        st.session_state.selectedSignal = signalDict['name']

    def add_generated_signal_name(self, sObject):
        for i in st.session_state.generatedSignals:
            if i['name'] == sObject['name']:
                flag = False
                sObject['name'] = sObject['name'] + \
                    ' {}'.format(st.session_state.generatedSignalCounter)
                st.session_state.generatedSignalCounter += 1
                break
        st.session_state.generatedSignals.append(sObject)

    def reset_values(self):
        st.session_state["sampling_slider"] = 0
        st.session_state["SNR_slider"] = 0

