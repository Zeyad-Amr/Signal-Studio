import streamlit as st
from stateManagement.stateManagement import stateManagement


class deleteWidget:
    def __init__(self):

        # stateManagement
        state = stateManagement()

        signalsList = []
        for signal in st.session_state.signalsList:
            signalsList.append(signal)

        with st.form("deleteSignals", clear_on_submit=True):
            selectedSignals = []
            for signal in range(len(signalsList)):
                checkboxVal = st.checkbox(
                    signalsList[signal]['name'])
                if checkboxVal:
                    selectedSignals.append(signalsList[signal])
            submittedDeleteBtn = st.form_submit_button("Delete")
            if submittedDeleteBtn:
                state.delete_signals(selectedSignals)
