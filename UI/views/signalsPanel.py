from ui.widgets.uploadWidget import uploadWidget
from ui.widgets.generateWidget import generateWidget
from ui.widgets.signalsListWidget import signalsListWidget
from ui.widgets.deleteWidget import deleteWidget
from ui.widgets.addWidget import addWidget
import streamlit as st


class signalsPanel:
    def __init__(self):

        uploadTab, generateTab = st.tabs(["Upload", "Generate"])
        with uploadTab:
            uploadWidget()

        with generateTab:
            generateWidget()

        signalsList, deleteSignals, addSignals = st.tabs(
            ["Signals", "Delete", "Add"])

        with signalsList:
            signalsListWidget()
        with deleteSignals:
            deleteWidget()
        with addSignals:
            addWidget()
