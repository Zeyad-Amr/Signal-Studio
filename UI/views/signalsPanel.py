from ui.widgets.uploadWidget import uploadWidget
from ui.widgets.generateWidget import generateWidget
from ui.widgets.signalsListWidget import signalsListWidget
from ui.widgets.deleteWidget import deleteWidget
from ui.widgets.addWidget import addWidget
import streamlit as st


class signalsPanel:
    def __init__(self):

        generateTab, uploadTab = st.tabs(["Generate", "Upload"])
        with uploadTab:
            uploadWidget()

        with generateTab:
            generateWidget()
            

        signalsList, deleteSignals = st.tabs(
            ["Signals", "Delete"])

        with signalsList:
            addWidget()
        with deleteSignals:
            deleteWidget()
            
