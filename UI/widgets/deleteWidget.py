import streamlit as st
from stateManagement.stateManagement import stateManagement


class deleteWidget:
    def __init__(self):

        # stateManagement
        state = stateManagement()

        signalsList = []
        for signal in st.session_state.signalsList:
            signalsList.append(signal['name'])

        with st.form("deleteSignals", clear_on_submit=True):
            selectedSignals = []
            for signal in range(len(signalsList)):
                checkboxVal = st.checkbox(
                    signalsList[signal], key=signalsList[signal] + 'ToDEL{}'.format(signal))
                if checkboxVal:
                    selectedSignals.append(self.signalsList[signal])
            submittedDeleteBtn = st.form_submit_button("Delete")
            # if submittedDeleteBtn:
            #     st.session_state.viewDeletePanel = False
            #     state.delete_signals(selectedSignals)
