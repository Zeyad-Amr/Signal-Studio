import os
from pathlib import Path
from click import clear
from numpy import sign
from werkzeug.utils import secure_filename
import streamlit as st
import os
from asyncio.windows_events import NULL


class leftNavBar:
    def __init__(self):
        with open("./styles/style.css") as source:
            style = source.read()
        st.markdown(f"""
        <style>
        {style}
        </style>
        """, unsafe_allow_html=True)

        uploadTab, generateTab = st.tabs(["Upload", "Generate"])

        if 'signalCounter' not in st.session_state:
            st.session_state.signalCounter = 0

        with uploadTab:
            uploadSignal = st.file_uploader("Upload Signal", type=["csv"], key='uploadButton')
            if uploadSignal:
                path = self.save_file(uploadSignal)
                siganlDict = st.session_state.signalObject.reading_signal(path)
                self.add_button(siganlDict)

        with generateTab:
            with st.form("generate_signal"):
                st.write("Generate Signal")
                signalTitle = st.text_input("Signal Title")

                freqVal = st.number_input("Frequency", )
                ampVal = st.number_input("Amplitude")
                phaseVal = st.number_input("Phase")

                submitted = st.form_submit_button("Generate")
                if submitted:
                    try:
                        siganlObject = st.session_state.signalObject.generate_signal(ampVal, freqVal, phaseVal)
                        if signalTitle:
                            self.add_button({
                                "name": signalTitle,
                                "signal": siganlObject
                            })
                        else:
                            self.add_button({
                                "name": "Untitled {}".format(st.session_state.signalCounter),
                                "signal": siganlObject
                            })
                            st.session_state.signalCounter += 1
                        st.success("Generated Successfully")
                    except:
                        st.error("Can't Generate Signal with these values...")

        signalsLst = []
        for signal in st.session_state.signals:
            signalsLst.append(signal['name'])

        st.radio("Signals", signalsLst, key="selectedSignal")

        if st.session_state.selectedSignal:
            self.on_change()

    def on_change(self):
        try:
            for signal in st.session_state.signals:
                if signal['name'] == st.session_state.selectedSignal:
                    st.session_state.signal = signal['signal']
                    st.session_state.graphWidget.draw_signal()
                    st.session_state.fileToDownload = signal['signal'].to_csv()
                    st.session_state.fileToDownloadName = signal['name']
                    # TODO: Select the last signal
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
        st.session_state.signals.append(signalDict)
        st.session_state.siganl = signalDict['signal']
