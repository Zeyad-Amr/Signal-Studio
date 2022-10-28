from UI.widgets.uploadWidget import uploadWidget
from UI.widgets.generateWidget import generateWidget
from UI.widgets.signalsListWidget import signalsListWidget
from UI.widgets.deleteWidget import deleteWidget
from UI.widgets.addWidget import addWidget
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
            
