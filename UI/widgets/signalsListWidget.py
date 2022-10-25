import streamlit as st
from stateManagement.stateManagement import stateManagement


class signalsListWidget:
    def __init__(self):

        # stateManagement
        state = stateManagement()

        self.signalsLst = ["Signal 1", "Signal 2", "Signal 3",
                           "Signal 4", "Signal 5", "Signal 6", "Signal 7", "Signal 8"]
        for signal in st.session_state.signals:
            self.signalsLst.append(signal['name'])

        st.radio("dd", self.signalsLst, key="selectedSignal",
                 on_change=state.on_change_radio)

        if st.session_state.selectedSignal:
            state.on_change()
