from ui.widgets.uploadWidget import uploadWidget
from ui.widgets.generateWidget import generateWidget
from ui.widgets.signalsListWidget import signalsListWidget
from ui.widgets.deleteWidget import deleteWidget
from ui.widgets.addWidget import addWidget
import streamlit as st


class signalsPanel:
    def __init__(self):
        st.write("Generate Signal")
        st.write("---")
        generateWidget()

        signalsList, deleteSignals = st.tabs(
            ["Signals", "Delete"])

        with signalsList:
            addWidget()
        with deleteSignals:
            deleteWidget()
