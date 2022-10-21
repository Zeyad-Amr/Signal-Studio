import os
from pathlib import Path
from click import clear
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

        tab1, tab2 = st.tabs(["Upload", "Generate"])

        with tab1:
            # signal file upload
            uploadSignal = st.file_uploader("Upload Signal", type=["csv"], key='uploadButton')
            if uploadSignal:
                path = self.save_file(uploadSignal)
                siganlDict = st.session_state.signalObject.reading_signal(path)
                st.session_state.header.add_button(siganlDict)

        with tab2:
            # generate signal
            with st.form("generate_signal"):
                st.write("Generate Signal")
                signalTitle = st.text_input("Signal Title")

                freqVal = st.number_input("Frequency")
                ampVal = st.number_input("Amplitude")
                phaseVal = st.number_input("Phase")

                submitted = st.form_submit_button("Generate")
                if submitted:
                    # TODO: Generate signal function
                    print(signalTitle, ", ", freqVal, ", ", ampVal, ", ", phaseVal)
                    st.success("Generated Successfully")

        signalsLst = []
        for signal in st.session_state.signals:
            signalsLst.append(signal['name'])


        st.radio("Signals", signalsLst, key="selectedSignal")

        if st.session_state.selectedSignal:
            self.on_change()

    def on_change(self):
        for signal in st.session_state.signals:
            if signal['name'] == st.session_state.selectedSignal:
                st.session_state.signal = signal['signal']
                st.session_state.graphWidget.draw_signal()

    def save_file(self, csvFile):
        try:
            filePath = os.path.join(
                Path(__file__).parent.parent, 'uploads', secure_filename(csvFile.name))

            with open(filePath, "wb") as file:
                file.write(csvFile.getbuffer())

            return filePath
        except:
            raise ValueError("Can't Upload this file, please try again...")
