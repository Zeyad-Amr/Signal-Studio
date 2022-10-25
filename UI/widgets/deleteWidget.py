import streamlit as st
from stateManagement.stateManagement import stateManagement


class deleteWidget:
    def __init__(self):

        # stateManagement
        state = stateManagement()

        self.signalsLst = ["Signal 1", "Signal 2", "Signal 3",
                           "Signal 4", "Signal 5", "Signal 6", "Signal 7", "Signal 8"]
        for signal in st.session_state.signals:
            self.signalsLst.append(signal['name'])

        with st.form("deleteSignals", clear_on_submit=True):
            selectedSignals = []
            for signal in range(len(self.signalsLst)):
                checkboxVal = st.checkbox(
                    self.signalsLst[signal], key=self.signalsLst[signal] + 'ToDEL{}'.format(signal))
                if checkboxVal:
                    selectedSignals.append(self.signalsLst[signal])
            submittedDeleteBtn = st.form_submit_button("Delete")
            if submittedDeleteBtn:
                st.session_state.viewDeletePanel = False
                state.delete_signals(selectedSignals)
                # if len(st.session_state.signals)!=0:
                st.experimental_rerun()
