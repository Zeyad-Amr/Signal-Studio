import streamlit as st
from stateManagement.stateManagement import stateManagement


class addWidget:
    def __init__(self):

        # stateManagement
        state = stateManagement()

        selectedSignals = []
        for signal in st.session_state.signalsList:
            checkboxVal = st.checkbox(
                signal['name'], key=signal['name'])
            if checkboxVal:
                selectedSignals.append(signal)

        st.session_state.selectedSignals = selectedSignals

        if len(selectedSignals) > 0:
            st.session_state.Mode = 2

        if st.session_state.Mode == 2:
            state.set_add_signals()